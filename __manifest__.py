{
    'name': 'Learning management System',
    'version': '1.0',
    'category': 'Education',
    'description': """The learning management (LSM) Application is a 
    web-based platform designed to manage online educational courses.""",
    
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/lms_views.xml',
        'views/lms_course_types_view.xml',
        'views/lms_assignment_view.xml',
        'views/lms_enrollment_view.xml',
        'views/lms_menu_view.xml',
    
    ],
    'installable': True,
    'application' : True,
}