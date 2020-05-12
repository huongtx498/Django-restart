from django import forms
MAU_SAC = [('Đỏ', 'Đỏ'), ('Vàng', 'Vàng'), ('Trắng', 'Trắng')]


class HomeForm(forms.Form):
    ten = forms.CharField(label="Giống chó: ", max_length=100)
    kichthuoc = forms.CharField(label="Kích thước (cm): ", max_length=100)
    # mausac = forms.CharField(label="Màu sắc: ", max_length=100)
    mausac = forms.ChoiceField(label="Màu sắc", choices=MAU_SAC)
    phukien = forms.CharField(label="Phụ kiện: ", max_length=100)
    anh = forms.ImageField(label="Ảnh:")
