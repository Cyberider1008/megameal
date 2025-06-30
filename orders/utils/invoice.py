from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def generate_invoice(order):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica", 14)

    p.drawString(100, 800, f"MegaMeal Invoice")
    p.drawString(100, 780, f"Order ID: {order.id}")
    p.drawString(100, 760, f"Customer: {order.customer.email}")
    p.drawString(100, 740, f"Total: ₹{order.total_price}")

    y = 700
    for item in order.items.all():
        p.drawString(100, y, f"{item.product.name} x{item.quantity} - ₹{item.price}")
        y -= 20

    p.drawString(100, y - 40, "Thank you for ordering with MegaMeal!")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
