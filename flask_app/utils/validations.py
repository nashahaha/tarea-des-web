import re
import filetype

def validate_name(name):
    valid_name = re.compile(r"^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$")
    return name!=None and len(name)>=3 and len(name)<=80 and valid_name.match(name)

def validate_email(email):
    valid_email = re.compile(r"^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$")
    return email!=None and valid_email.match(email) and (email.count("@")==1)

def validate_phone(phone):
    valid_phone = re.compile(r"^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$")
    return valid_phone.match(phone)

def validate_device_name(device):
    return device!=None and len(device)>=3 and len(device)<=80

def validate_description(description):
    return description<=500

def validate_years(years):
    return years!=None and years>=1 and years<=99 and type(years)==int

def validate_file(file):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if file is None:
        return False

    # check if the browser submitted an empty file
    if file.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(file)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_select(select):
    if not select: False
    else: True

def validate_user(name, email, phone, region, comuna):
    return validate_name(name) and validate_email(email) and validate_phone(phone) and validate_select(region) and validate_select(comuna)

def validate_device(device, description, type, years, status, pics):
    for pic in pics:
        if not validate_file(pic):
            return False
    return validate_device(device) and validate_description(description) and validate_select(type) and validate_years(years) and validate_select(status)

