from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from backend import db
from backend.models.tutor import  Tutor

tutors = Blueprint('tutors', __name__,url_prefix="/tutors")



#retrieving all tutors 
@tutors.route("/", methods=['GET'])
def all_tutors():
    #ensuring that a user has logged in
    all_tutors = Tutor.query.all()
    return jsonify(all_tutors),200


#retrieving all tutors for a user
@tutors.route("/users/<int:user_id>", methods=['GET'])
@jwt_required()
def all_user_tutors(user_id):
    #ensuring that a user has logged in
    user_id= get_jwt_identity()
    all_tutors = Tutor.query.filter_by(id=user_id).all()
    return jsonify(all_tutors),200


#retrieving single tutors 
@tutors.route("/<int:tutorId>", methods=['GET'])
def single_tutor(tutorId):
    single_tutor = Tutor.query.filter_by(id=tutorId).first()
    
    #Question that does'nt exist
    if not single_tutor:
        return jsonify({'message': '  Tutor not found'}), 404
    return jsonify(single_tutor),200



#creating tutors
@tutors.route("/", methods=["POST"])
@jwt_required()
def new_tutors():
    
    if request.method == "POST":
        
        user_id = get_jwt_identity()
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        contact= request.json['contact']
        


       #empty fields for validation
      
        if not name:
                 
          return jsonify({'error': 'Please provide your name'}), 400 #bad request
          
        if not email:
                return jsonify({'error': 'Please provide your email'}), 400
        #empty fields
      

          
        if not password:
                return jsonify({'error': 'Please provide your password '}), 400
            
        if not contact:
                return jsonify({'error': 'Please provide your contact '}), 400
        
        #checking if name exists
        if Tutor.query.filter_by(name=name).first():
                return jsonify({
                'error': 'Name exists'
            }), 409 #conflicts
        
        #checking if email exists
        if Tutor.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Email already exists'
            }), 409
        
           

        #inserting values into the tutors_list
        new_tutor = Tutor(name=name,email=email,user_id=user_id,password=password,contact=contact)
        db.session.add(new_tutor)
        db.session.commit()
        
         
  
    return jsonify({'message':'new tutor added','name':name,'email':email,'password':password,'user_id':user_id,'contact':contact}),200
    


 
# #deleting a tutor
@tutors.route("/remove/<string:tutorId>", methods=['DELETE'])
@jwt_required()
def delete_tutors(tutorId):
    current_user = get_jwt_identity()

    tutor = Tutor.query.filter_by(user_id=current_user, id=tutorId).first()

    if not tutor:
        return jsonify({'message': 'Tutor not found'}), 404

    db.session.delete(tutor)
    db.session.commit()

    return jsonify({}), 204

    



