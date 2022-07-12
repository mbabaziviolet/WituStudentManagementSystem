from flask import  jsonify, request, Blueprint
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


#retrieving single admins item
@admins.route("/<int:adminId>", methods=['GET'])
def single_admin(adminId):
    single_admin = Admin.query.filter_by(id=adminId).first()
    
    #Admin that does'nt exist
    if not single_admin:
        return jsonify({'message': '  Admin not found'}), 404
    return jsonify(single_admin),200


#retrieving single admins item for a user
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
        
       
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password'] 
        
        
       
       

       #empty fields
      
        if not title:
                 
          return jsonify({'error': 'Please provide a title for the Admin'}), 400 #bad request
          
        if not body:
                return jsonify({'error': 'Please provide a body for the Admin'}), 400
        #empty fields
      

          
        if not tag:
                return jsonify({'error': 'Please add a tag for the Admin ie python '}), 400
        
        #checking if title exists
        if Admin.query.filter_by(title=title).first():
                return jsonify({
                'error': 'Admin title exists'
            }), 409 #conflicts
        
        #checking if body exists
        if Admin.query.filter_by(body=body).first():
                return jsonify({
                'error': 'Admin body already exists'
            }), 409
        
           

        #inserting values into the Admins_list
        new_Admin = Admin(title=title,body=body,user_id=user_id,tag=tag)
        db.session.add(new_Admin)
        db.session.commit()
        
         
  
    return jsonify({'message':'new Admin posted','tag':tag,'title':title,'body':body,'user_id':user_id}),200
    


 
# #deleting a Admin
@Admins.route("/remove/<string:AdminId>", methods=['DELETE'])
@jwt_required()
def delete_Admins(AdminId):
    current_user = get_jwt_identity()

    Admin = Admin.query.filter_by(user_id=current_user, id=AdminId).first()

    if not Admin:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(Admin)
    db.session.commit()

    return jsonify({}), 204

    


#creating answers
@Admins.route("/<int:Admin_id>/answers", methods=["POST"])
@jwt_required()
def new_answers(Admin_id):
    if request.method == "POST":
        
        Admin_id =  request.json['Admin_id']
        user_id = get_jwt_identity()
        body = request.json['body']
        
        if not body:
            return jsonify({'error':'Please provide your content for the answer'}), 400
        
        if not Admin_id:
            return jsonify({'error':'An id for the Admin being replied to is required'}), 400
        
        #checking if body exists
        if Answer.query.filter_by(body=body).first():
                return jsonify({
                'error': 'This answer already exists'
            }), 409
        
           

        #inserting values into the Admins_list
        new_answer = Answer(Admin_id= int(Admin_id),body=body,user_id=user_id)
        db.session.add(new_answer)
        db.session.commit()
       
         
  
    return jsonify({'message':'new answer posted','Admin_id':Admin_id,'body':body,'user_id':user_id}),200
    

#Viewing an answer by id
@Admins.route("/<int:answer_id>/answers")
@jwt_required()
def single_answer(answer_id):
    single_answer = Answer.query.filter_by(id=answer_id).first()
  
    return jsonify(single_answer),200

#retrieving all answers for a specific user
@Admins.route("/answers/<int:user_id>")
@jwt_required()
def user_answers(user_id):
    #ensuring that a user has logged in
    user_id = get_jwt_identity()
    answers = Answer.query.filter_by(user_id=user_id).first()
    return jsonify(answers),200



#retrieving all answers
@Admins.route("/answers", methods=['GET'])
def all_answers():
    all_answers = Answer.query.all()
    return jsonify(all_answers),200