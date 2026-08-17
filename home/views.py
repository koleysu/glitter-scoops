import random
import json
import os
import uuid
import os
import json
import uuid
from datetime import datetime
from urllib.parse import quote
from django.shortcuts import render
from urllib.parse import quote
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.conf import settings
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        ).strip()


        # ---------------------------------------
        # Staff Users File
        # ---------------------------------------

        file_path = settings.STAFF_USERS_FILE

        users = []


        if os.path.exists(file_path):

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    users = json.load(f)

            except json.JSONDecodeError:

                users = []


        # ---------------------------------------
        # Validate User
        # ---------------------------------------

        for user in users:

            stored_username = user.get(
                "username",
                ""
            ).strip()

            stored_password = user.get(
                "password",
                ""
            ).strip()

            active = user.get(
                "active",
                False
            )


            # Username
            if stored_username.lower() != \
                    username.lower():

                continue


            # Active User
            if not active:

                continue


            # Password
            if password != stored_password:

                continue


            # -----------------------------------
            # Login Successful
            # -----------------------------------

            request.session[
                "staff_logged_in"
            ] = True

            request.session[
                "staff_username"
            ] = stored_username

            request.session[
                "staff_name"
            ] = user.get(
                "name",
                stored_username
            )


            return redirect("/orders/")


        # ---------------------------------------
        # Login Failed
        # ---------------------------------------

        return render(
            request,
            "home/login.html",
            {
                "error":
                    "Invalid username or password."
            }
        )


    return render(
        request,
        "home/login.html"
    )
    
def logout_view(request):

    request.session.pop(
        "staff_logged_in",
        None
    )

    request.session.pop(
        "staff_username",
        None
    )

    request.session.pop(
        "staff_name",
        None
    )

    return redirect("/login/")

def create_staff_user(username, password, name):

    file_path = os.path.join(
        os.path.dirname(__file__),
        "database",
        "staff_users.json"
    )

    os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True
    )

    # Read existing users
    if os.path.exists(file_path):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                users = json.load(f)

        except json.JSONDecodeError:

            users = []

    else:

        users = []


    # Check duplicate username
    for user in users:

        if user["username"].lower() == username.lower():

            return False


    # Create user
    new_user = {

        "username": username,

        "password": make_password(password),

        "name": name,

        "active": True

    }


    users.append(new_user)


    # Save
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            users,
            f,
            indent=4
        )


    return True
def orders(request):

    if not request.session.get("staff_logged_in"):

        return redirect(
            "/login/?next=/orders/"
        )


    # Your existing orders code
    # -------------------------

    file_path = os.path.join(
        os.path.dirname(__file__),
        "database",
        "orders.json"
    )

    orders_data = []

    if os.path.exists(file_path):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                orders_data = json.load(f)

        except json.JSONDecodeError:

            orders_data = []


    return render(
        request,
        "home/orders.html",
        {
            "orders": orders_data
        }
    )
# 🔹 MENU PAGE
def menu(request):
    
    """
    Load products from database/products.json
    and prepare them for menu.html.
    """

    products_file = os.path.join(
        os.path.dirname(__file__),
        "database",
        "products.json"
    )

    # Load products
    if os.path.exists(products_file):

        with open(products_file, "r", encoding="utf-8") as f:
            items = json.load(f)

    else:
        items = []

    # Prepare data for template
    for item in items:
    

        # Popup required or not
        item["popup_required"] = item.get(
            "popup_required",
            False
        )

        # Product Description
        item["desc"] = item.get(
            "description",
            f"{item['name']} - {item.get('category', '')}"
        )

        # Default Variant
        if item.get("variants"):

            item["default_variant"] = item["variants"][0]

            item["price"] = item["default_variant"]["price"]

        else:

            item["default_variant"] = None

            item["price"] = 0
        item["json_data"] = json.dumps(item)
    # Send complete product list to JavaScript
    products_json = json.dumps(items)

    return render(
        request,
        "home/menu.html",
        {
            "items": items,
            "products_json": products_json
        }
    )



#Save Order




def save_orders(request):
    print(request.POST)
    if request.method != "POST":
        return redirect("orders")
    if request.method == "POST":

        file_path = os.path.join(
            os.path.dirname(__file__),
            "database",
            "orders.json"
        )

        with open(file_path, "r") as f:
            orders = json.load(f)

        total = int(request.POST.get("total_orders"))

        for i in range(total):

            order_id = request.POST.get(f"order_id_{i}")

            status = request.POST.get(f"status_{i}")

            delivered = request.POST.get(f"delivered_{i}")

            for order in orders:

                if order["order_id"] == order_id:

                    order["status"] = status

                    if delivered == "on":

                        order["status"] = "Delivered"

                        order["delivery_date"] = datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                        order["payment_status"] = "Paid"

        with open(file_path, "w") as f:

            json.dump(orders, f, indent=4)

        return redirect("/orders/")



def cart(request):
    return render(request, "home/cart.html")
# 🔹 CHECKOUT PAGE


def order_confirmation(request):

    order=request.session.get("order")

    return render(
        request,
        "home/order_confirmation.html",
        {
            "order":order
        }
    )





def checkout(request):

    if request.method == "POST":

        # =====================================================
        # 1. CUSTOMER DETAILS
        # =====================================================

        customer = {
            "name": request.POST.get("name", "").strip(),
            "gender": request.POST.get("gender", "").strip(),
            "age": request.POST.get("age", "").strip(),
            "mobile": request.POST.get("mobile", "").strip(),
            "whatsapp": request.POST.get("whatsapp", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "address": request.POST.get("address", "").strip(),
        }


        # =====================================================
        # 2. GET CART DATA FROM CHECKOUT FORM
        # =====================================================

        cart_data = request.POST.get("cart_data", "")

        print("===================================")
        print("CART DATA RECEIVED:")
        print(cart_data)
        print("===================================")


        # =====================================================
        # 3. CONVERT CART JSON INTO PYTHON DICTIONARY
        # =====================================================

        try:

            if cart_data:
                cart = json.loads(cart_data)
            else:
                cart = {}

        except json.JSONDecodeError:

            print("ERROR: Invalid cart JSON")

            cart = {}


        # =====================================================
        # 4. PROCESS CART ITEMS
        # =====================================================

        items = []
        grand_total = 0


        for item in cart.values():

            try:

                price = float(item.get("price", 0))
                qty = int(item.get("qty", 0))

            except (ValueError, TypeError):

                continue


            if qty <= 0:
                continue


            item_total = price * qty

            grand_total += item_total


            items.append({

                "name": item.get("name", ""),

                "price": price,

                "qty": qty,

                "image": item.get("image", ""),

                "total": item_total

            })


        # =====================================================
        # 5. DEBUG INFORMATION
        # =====================================================

        print("NUMBER OF ITEMS:", len(items))
        print("ITEMS:", items)
        print("GRAND TOTAL:", grand_total)


        # =====================================================
        # 6. CREATE ORDER
        # =====================================================

        order = {

            "order_id":
                str(uuid.uuid4())[:8].upper(),

            "customer": {

                "name": customer["name"],

                "gender": customer["gender"],

                "age":
                    int(customer["age"])
                    if customer["age"]
                    else 0,

                "mobile": customer["mobile"],

                "whatsapp": customer["whatsapp"],

                "email": customer["email"],

                "address": customer["address"]

            },

            "items": items,

            "grand_total": grand_total,

            "order_date":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "payment_status": "Pending",

            "status": "Pending"

        }


        # =====================================================
        # 7. SAVE ORDER TO orders.json
        # =====================================================

        file_path = os.path.join(

            os.path.dirname(__file__),

            "database",

            "orders.json"

        )


        os.makedirs(

            os.path.dirname(file_path),

            exist_ok=True

        )


        # Read existing orders

        if os.path.exists(file_path):

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    orders = json.load(f)

                    if not isinstance(orders, list):
                        orders = []

            except (json.JSONDecodeError, FileNotFoundError):

                orders = []

        else:

            orders = []


        # Add new order

        orders.append(order)


        # Save orders

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                orders,
                f,
                indent=4,
                ensure_ascii=False
            )


        # =====================================================
        # 8. WHATSAPP
        # =====================================================

        whatsapp = "".join(

            filter(
                str.isdigit,
                customer["whatsapp"]
            )

        )


        if len(whatsapp) == 10:

            whatsapp = "91" + whatsapp


        message = f"""
✨ Glitter Scoops ✨

Thank you {customer['name']}.

Order ID : {order['order_id']}

Items : {len(items)}

Grand Total : ₹{grand_total}

Your order has been received successfully.
"""


        whatsapp_url = (

            f"https://wa.me/{whatsapp}"

            f"?text={quote(message)}"

        )


        # =====================================================
        # 9. STORE ORDER IN SESSION
        # =====================================================

        request.session["order"] = order


        # =====================================================
        # 10. REDIRECT TO WHATSAPP PAGE
        # =====================================================

        return render(

            request,

            "home/redirect_whatsapp.html",

            {
                "url": whatsapp_url
            }

        )


    # =========================================================
    # GET REQUEST
    # =========================================================

    return render(
        request,
        "home/checkout.html"
    )