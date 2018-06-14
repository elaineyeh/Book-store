from django import forms as f


class PaidConfirmForm(f.Form):
    check = f.BooleanField(label='我確定要結帳')

class DeleteConfirmForm(f.Form):
    check = f.BooleanField(label='確定刪除')
