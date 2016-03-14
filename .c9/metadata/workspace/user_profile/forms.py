{"filter":false,"title":"forms.py","tooltip":"/user_profile/forms.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":68,"column":32},"action":"insert","lines":["from django import forms","from django.contrib.auth.models import User","","class ProfileForm(forms.ModelForm):","    ","    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=30,","        required=False)","    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=30,","        required=False)","    job_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=50,","        required=False)","    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),","        max_length=75,","        required=False)","    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=50,","        required=False)","    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=50,","        required=False)","","    class Meta:","        model = User","        fields = ['first_name', 'last_name', 'job_title', 'email', 'url', 'location',]","","    def full_clean(self):","        'Strip whitespace automatically in all form fields'","        data = self.data.copy()","        for k, vs in self.data.lists():","            new_vs = []","            for v in vs:","                new_vs.append(v.strip())","            data.setlist(k, new_vs)","        self.data = data","        super(ProfileForm, self).full_clean()","","","class ChangePasswordForm(forms.ModelForm):","    id = forms.CharField(widget=forms.HiddenInput())","    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), ","        label=\"Old password\",","        required=True)","","    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), ","        label=\"New password\",","        required=True)","    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), ","        label=\"Confirm new password\",","        required=True)","","    class Meta:","        model = User","        fields = ['id', 'old_password', 'new_password', 'confirm_password']","","    def clean(self):","        super(ChangePasswordForm, self).clean()","        old_password = self.cleaned_data.get('old_password')","        new_password = self.cleaned_data.get('new_password')","        confirm_password = self.cleaned_data.get('confirm_password')","        id = self.cleaned_data.get('id')","        user = User.objects.get(pk=id)","        if not user.check_password(old_password):","            self._errors['old_password'] = self.error_class(['Old password don\\'t match'])","        if new_password and new_password != confirm_password:","            self._errors['new_password'] = self.error_class(['Passwords don\\'t match'])","        return self.cleaned_data"],"id":1}],[{"start":{"row":11,"column":4},"end":{"row":13,"column":23},"action":"remove","lines":["job_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=50,","        required=False)"],"id":2}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":10,"column":23},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":14,"column":4},"end":{"row":16,"column":23},"action":"remove","lines":["url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), ","        max_length=50,","        required=False)"],"id":5}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":13,"column":23},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":["'"],"id":8}],[{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"remove","lines":["e"],"id":9},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"remove","lines":["l"]}],[{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"remove","lines":["t"],"id":10}],[{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"remove","lines":["i"],"id":11}],[{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"remove","lines":["t"],"id":12}],[{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"remove","lines":["_"],"id":13}],[{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["b"],"id":14}],[{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"remove","lines":["o"],"id":15}],[{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"remove","lines":["j"],"id":16}],[{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"remove","lines":["'"],"id":17}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"remove","lines":[" "],"id":18},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"remove","lines":[","]}],[{"start":{"row":20,"column":59},"end":{"row":20,"column":60},"action":"remove","lines":[","],"id":19}],[{"start":{"row":20,"column":58},"end":{"row":20,"column":59},"action":"remove","lines":["'"],"id":20}],[{"start":{"row":20,"column":57},"end":{"row":20,"column":58},"action":"remove","lines":["l"],"id":21}],[{"start":{"row":20,"column":56},"end":{"row":20,"column":57},"action":"remove","lines":["r"],"id":22}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":["u"],"id":23}],[{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"remove","lines":["'"],"id":24}],[{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"remove","lines":[" "],"id":25}]]},"ace":{"folds":[],"scrolltop":761,"scrollleft":0,"selection":{"start":{"row":20,"column":53},"end":{"row":20,"column":53},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1456857725153,"hash":"39e076357ddd577f6fb7659d99684e5f5b1c13f5"}