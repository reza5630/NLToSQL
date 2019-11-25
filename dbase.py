'''
dbaseSchema = {'employee':["employee name","street", "city"],
               'works':['employee name','company name','salary'],
               'company':['company name','city'],
               'manages':["employee name",'manager name']}

meta_data =   {'employee':'employee','employee.employeename':"name",'employee.street':"street address",'employee.city':"city town",
               'works':'works','works.employeename':'name','works.companyname':'company name','works.salary':'salary',
               'company':'company','company.companyname':'name','company.city':'city',
               'manages':'manages','manages.employeename':"name",'manages.managername':'name'}


dbaseSchema = { 'person':[ "driver id", "name", "address"],
                'car' : ['possessor','license', 'model', 'year',"driver id"],
                'accident': ['report', 'number', 'date', 'location',"driver id"],
                'participated': ['report number', 'license', 'driver id', 'damage amount']}

meta_data =   { 'person': 'person people',"person.driverid":'number', "person.name":'name', "person.address":'address street',
                'car':'car','car.possessor':'possessor owner','car.license':'license registration','car.model':'type model',
                'car.year':'year','car.driverid':'number','accident.report':'report','accident.number':'number',
                'accident.date':'date', 'accident.location':'location place','accident.driverid':'number','accident':'accident',
                'participated':'participated', 'participated.reportnumber':'number', 'participated.license':'license registration',
                'participated.driverid':'number', 'participated.damageamount':'damage amount'}

dbaseSchema = { 'classroom':["building", "room number", "capacity"],
                'department':['dept name', "building","budget"],
                'course':['course id', 'title', 'dept name', 'credits'],
                'instructor':['ID', 'name', 'dept name', 'salary'],
                'section':['course id', 'sec id', 'semester', 'year', 'building', 'room number', 'time slot id'],
                'teaches':['ID', 'course id', 'sec id', 'semester', 'year'],
                'student':['ID', 'name', 'dept name', 'tot cred'],
                'takes':['ID', 'course id', 'sec id', 'semester', 'year', 'grade'],
                'advisor':['s ID', 'i ID'],
                'time slot':['time slot id', 'day', 'start time', 'end time'],
                'prereq':['course id', 'prereq id']}

meta_data =  { 'classroom':'classroom',"classroom.building":'', "classroom.roomnumber":'', "classroom.capacity":'',
                'department':'department','department.deptname':'', "department.building":'',"department.budget":'',
                'course':'','course.courseid':'', 'course.title':'', 'course.deptname':'', 'course.credits':'',
                'instructor':'','instructor.ID':'', 'instructor.name':'', 'instructor.deptname':'', 'instructor.salary':'',
                'section':'','section.courseid':'', 'section.secid':'', 'section.semester':'',
                'section.year':'', 'section.building':'', 'section.roomnumber':'', 'section.timeslotid':'',
                'teaches':'','teaches.ID':'', 'teaches.course id':'', 'teaches.sec id':'', 'teaches.semester':'', 'teaches.year':'',
                'student':'','student.ID':'', 'student.name':'', 'student.dept name':'', 'student.tot cred':'',
                'takes':'takes','takes.ID':'', 'takes.course id':'', 'takes.sec id':'', 'takes.semester':'', 'takes.year':'', 'takes.grade':'',
                'advisor':'advisor','advisor.sID':'student', 'advisor.iID':'instructor',
                'timeslot':'timeslot','timeslot.time slot id':'', 'timeslot.day':'', 'timeslot.start time':'', 'timeslot.end time':'',
                'prereq':'prereq','prereq.course id':'', 'prereq.prereq id':''}


dbaseSchema = {'branch': ["branch name", "branch city", "assets"],
               'customer': ["customer name", "customer street", "customer city"],
               'loan': ["loan number", "branch name", "amount"],
               'borrower': ["customer name", "loan number"],
               'account': ["account number", "branch name", "balance"],
               'depositor': ["customer name", "account number"]}

meta_data = {'branch':'branch', "branch.branchname":'name', "branch.branchcity":'city', "branch.assets":'assets',
             'customer':'customer', "customer.customername":'name', "customer.customerstreet":'strret', "customer.customercity":'city',
             'loan':'loan', "loan.loannumber":'number', "loan.branchname":'branch name', "loan.amount":'amount',
             'borrower':'borrower', "borrower.customername":'name', "borrower.loannumber":'number',
             'account':'account branch', "account.accountnumber":'number', "branch.branchname":'name', "branch.balance":'balance',
             'depositor':'depositor', "depositor.customername":'customer name', "depositor.accountnumber":'account number'}
'''
dbaseSchema = {'pers':["ID","fname", "lname", "age"],
                'cont':["phone 1", "phone 2", "address line 1","address line 2","zip code","person ID"],
                'log':["username", "password"]}

meta_data =    {'pers':'person personal Information','pers.ID':'number','pers.fname':'firstname first name','pers.lname':'lastname last name','pers.age':'age',
                'cont':'contact','cont.phone1':"primary phone number",'cont.phone2':'seconadary phone number' ,
                'cont.addressline1':"primary address",'cont.addressline2':"secondary address",'cont.zipcode':"zip code",
                'cont.personID':"person number",'log':'login','log.username':"username", 'log.password':"password"}
