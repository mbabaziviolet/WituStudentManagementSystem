from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from backend import db
from backend.models.students import Student

students = Blueprint('students', __name__,url_prefix="/students")



#retrieving all students 
@students.route("/", methods=['GET'])
def all_students():
    #ensuring that a user has logged in
    all_students = Student.query.all()
    return jsonify(all_students),200


#retrieving all students for a user
@students.route("/users/<int:user_id>", methods=['GET'])
@jwt_required()
def all_user_students(user_id):
    #ensuring that a user has logged in
    user_id= get_jwt_identity()
    all_students = Student.query.filter_by(id=user_id).all()
    return jsonify(all_students),200


#retrieving single student
@students.route("/<int:studentId>", methods=['GET'])
def single_student(studentId):
    single_student = Student.query.filter_by(id=studentId).first()
    
    #Student that does'nt exist
    if not single_student:
        return jsonify({'message': '  Student not found'}), 404
    return jsonify(single_student),200


#creating students
@students.route("/", methods=["POST"])
@jwt_required()
def new_students():
    
    if request.method == "POST":
        
        user_id = get_jwt_identity()
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        user_name = request.json['user_name']
        gender = request.json['gender']
        age = request.json['age']
        email = request.json['email']
        password = request.json['password']
        guardian_name = request.json['guardian_name']
        guardian_contact = request.json['guardian_contact']
        is_admitted = request.json['is_admitted']
        image = request.json['image']
       
       

       #empty fields
      
        if not first_name:
                 
          return jsonify({'error': 'Please provide your firstname'}), 400 #bad request
        if not last_name:
                 
          return jsonify({'error': 'Please provide your lastname'}), 400 #bad request
        if not user_name:
                 
          return jsonify({'error': 'Please provide your username'}), 400 #bad request
        if not email:
                 
          return jsonify({'error': 'Please provide your email'}), 400 #bad request
        if not password:
                 
          return jsonify({'error': 'Please provide your password'}), 400 #bad request
          
        if not gender:
                return jsonify({'error': 'Please provide your gender'}), 400
            
        if not age:
                return jsonify({'error': 'Please provide your age'}), 400
            
        if not guardian_name:
                return jsonify({'error': 'Please provide your guardian name'}), 400
            
        if not guardian_contact:
                return jsonify({'error': 'Please provide your guardian contact'}), 400
        
        if not image:
                return jsonify({'error': 'Please provide your image'}), 400
            
        #empty fields
    
        
        #checking if email exists
        if Student.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Email already exists'
            }), 409 #conflicts
        
        #checking if username exists
        if Student.query.filter_by(user_name=user_name).first():
                return jsonify({
                'error': 'Username already exists'
            }), 409
        
           

        #inserting values into the students_list
        new_student= Student(user_name=user_name,email=email,user_id=user_id,password=password,first_name=first_name,last_name=last_name,guardian_name=guardian_name,guardian_contact=guardian_contact,age=age,gender=gender,image=image,is_admitted=is_admitted)
        db.session.add(new_student)
        db.session.commit()
        
         
  
    return jsonify({'message':'new student created','user_name':user_name,'email':email,'user_id':user_id,'password':password,'first_name':first_name,'last_name':last_name,'guardian_name':guardian_name,'guardian_contact':guardian_contact,'age':age,'gender':gender,'image':image,'is_admitted':is_admitted}),200
    

#deleting a student
@students.route("/remove/<string:studentId>", methods=['DELETE'])
@jwt_required()
def delete_students(studentId):
    current_user = get_jwt_identity()

    student = Student.query.filter_by(user_id=current_user, id=studentId).first()

    if not student:
        return jsonify({'message': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({}), 204

    