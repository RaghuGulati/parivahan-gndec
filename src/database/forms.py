from django import forms
from .models import *
from phonenumber_field.modelfields import PhoneNumberField

class new_student(forms.Form):
    urn = forms.CharField(
		    widget=forms.NumberInput(
	            attrs={"class": "form-control",  "placeholder": "Enter University Roll Number"}),
	            required=True, label="URN",
		    )
    crn = forms.CharField(widget=forms.NumberInput(
	            attrs={ "class": "form-control", "placeholder": "Enter Class Roll Number"}
        	    ),
	            required=True,
		    label = "CRN",
		)

    name = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter Name",
            		}
        	    ),
	            required=True,
    		    max_length=50,
	    )
    fmname = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter Father's/Mother's Name",
            		}
        	    ),
	            required=True,
    		    max_length=50,
		    label = "Father/Mother's Name"
	    )

    mobile = forms.CharField(widget=forms.TextInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Student's Mobile Number",
            		}
        	    ),
	            required=True,
		    label = "Mobile Number",
)

    fmname = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter Father/Mother's Name",
            		}
        	    ),
	            required=True,
    		    max_length=25,
		    label = "Father/Mother's Name"
	    )
 

    email = forms.EmailField(
		    widget=forms.EmailInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Email ID",
            		}
        	    ),
	            required=True,
		    label = "Email ID",

		    max_length = 50
		    )

    address = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter address",
            		}
        	    ),
	            required=True,
    		    max_length=50,
		    label = "Address"
	    )

    aadhar_no = forms.CharField(widget=forms.NumberInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Aadhar Card Number",
            		}
        	    ),
	            required=True,
		    label = "Aadhar Number",

)
    choices = (('CE', 'Civil Engineering'),
	       ('EE', 'Electrical Engineering'),
	       ('ME', 'Mechanical Engineering'),
	       ('EC', 'Electronics and Communication Engineering'),
	       ('CS', 'Computer Science and Engineering'),
	       ('IT', 'Information Technology'),
	       ('PE', 'Production Engineering'),
	       ('MBA', 'Masters in Business Administration'),
	       ('MCA', 'Masters in Computer Applications'),
	      )
#    degree = forms.ChoiceField(choices=degree_choices)

    residence = (('Hosteler', 'Hosteler'),('Day Scholor','Day Scholor'))

    years = (('1','1st'),('2','2nd'),('3','3rd'),('4','4th'))
    branch = forms.CharField(widget=forms.Select(
			    	choices = choices,
				attrs = {
					 "class": "form-control",
					 "style": "height:50px;"

				}
			    )
		    )
    year = forms.CharField(widget=forms.Select(
			    	choices = years,
				attrs = {
					 "class": "form-control",
					 "style": "height:50px;"
				}
			    ))
    section = forms.CharField(widget=forms.TextInput(
				attrs = {
					 "class": "form-control",
					 "placeholder" : "Section",
				}
			    )
)
    residence = forms.ChoiceField(choices = residence,
		    	widget=forms.RadioSelect(
				attrs ={
					'id':'myid',

				} 
				),							
			label = 'Mode of residence'    
		    )
    photo = forms.FileField()
    
    def __init__(self, *args, **kwargs):
        super(new_student, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'*'.format(fieldname=field.label)}

	    
class new_care_taker(forms.Form):
    name = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter Name",
            		}
        	    ),
	            required=True,
    		    max_length=50,
	    )

    mobile = forms.CharField(widget=forms.TextInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Care Taker's Mobile Number",
            		}
        	    ),
	            required=True,
		    label = "Mobile Number",
	)
    email = forms.EmailField(
		    widget=forms.EmailInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Email ID",
            		}
        	    ),
	            required=True,
		    label = "Email ID",

		    max_length = 50
		    )

    choices = ((1,1),(2,2),(3,3),(4,4),(5,5))
    hostel_no = forms.CharField(widget=forms.Select(
			    	choices = choices,
				attrs = {
					 "class": "form-control",
					 "style": "height:50px;"

				}
			    )
		    )
   
    def __init__(self, *args, **kwargs):
        super(new_care_taker, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'*'.format(fieldname=field.label)}

class new_advisor(forms.Form):
    name = forms.CharField(
		    widget=forms.TextInput(
	            attrs={ "class": "form-control",
                	"placeholder": "Enter Name",
            		}
        	    ),
	            required=True,
    		    max_length=50,
	    )

    mobile = forms.CharField(widget=forms.TextInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Advisor's Mobile Number",
            		}
        	    ),
	            required=True,
		    label = "Mobile Number",
	)
    email = forms.EmailField(
		    widget=forms.EmailInput(
		    attrs={ "class": "form-control",
                	"placeholder": "Enter Email ID",
            		}
        	    ),
	            required=True,
		    label = "Email ID",

		    max_length = 50
		    )

    b = Student.objects.values_list('class_calculated', flat = True).distinct()
    choices = [(id,id) for id in b]

    class_alloted = forms.CharField(widget=forms.Select(
			    	choices = choices,
				attrs = {
					 "class": "form-control",
					 "style": "height:50px;"

				}
			    )
		    )
   
    def __init__(self, *args, **kwargs):
        super(new_advisor, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'*'.format(fieldname=field.label)}    
	    
