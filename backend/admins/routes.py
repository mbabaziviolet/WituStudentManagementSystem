from flask import  jsonify, request, Blueprint
from backend.auth.routes import user_id
from flask_jwt_extended import jwt_required,get_jwt_identity
from backend import db
from backend.models.admins import  Admin

admins = Blueprint('admins', __name__,url_prefix="/admins")



#retrieving all admins 
@admins.route("/", methods=['GET'])
def all_admins():
    #ensuring that a user has logged in
    all_admins = Admin.query.all()
    return jsonify(all_admins),200


#retrieving single admins 
@admins.route("/<int:adminId>", methods=['GET'])
def single_admin(adminId):
    single_admin = Admin.query.filter_by(id=adminId).first()
    
    #Admin that does'nt exist
    if not single_admin:
        return jsonify({'message': '  Admin not found'}), 404
    return jsonify(single_admin),200


#retrieving single admins for a user
@admins.route("/<string:adminId>", methods=['GET'])
@jwt_required()
def single_user_Admin(AdminId):
    current_user = get_jwt_identity()
    single_Admin = Admin.query.filter_by(user_id=current_user,id=AdminId).first()
    
    #if a Admin doesnt exist
    if not single_Admin:
        return jsonify({'message': '  Admin not found'}), 404
    return jsonify(single_Admin),200 


#creating admins
@admins.route("/", methods=["POST"])
@jwt_required()
def new_admins():
    
    if request.method == "POST":
        
        user_id=request.json['user_id']
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password'] 
        

       #empty fields
      
        if not name:
                 
          return jsonify({'error': 'Please provide a name for the Admin'}), 400 #bad request
          
        if not email:
                return jsonify({'error': 'Please provide a email for the Admin'}), 400
        #empty fields
      
        if not phone:
                return jsonify({'error': 'Please add a phone contact for the Admin '}), 400
            
        if not password:
                return jsonify({'error': 'Please add a password for the Admin  '}), 400
        
        
        #checking if name exists
        if Admin.query.filter_by(name=name).first():
                return jsonify({
                'error': 'Admin name exists'
            }), 409 #conflicts
        
        #checking if email exists
        if Admin.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Admin email already exists'
            }), 409
        
           

        #inserting values into the Admins_list
        new_Admin = Admin(name=name,email=email,user_id=user_id,password=password)
        db.session.add(new_Admin)
        db.session.commit()
        
         
  
    return jsonify({'message':'new Admin posted','name':name,'email':email,'password':password,'user_id':user_id}),200
    


 
# #deleting a Admin
@admins.route("/remove/<string:AdminId>", methods=['DELETE'])
@jwt_required()
def delete_Admins(AdminId):
    current_user = get_jwt_identity()

    Admin = Admin.query.filter_by(user_id=current_user, id=AdminId).first()

    if not Admin:
        return jsonify({'message': 'Admin not found'}), 404

    db.session.delete(Admin)
    db.session.commit()

    return jsonify({}), 204

    



