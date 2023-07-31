{
    'name': 'Learning management System',
    'version': '1.0',
    'category': 'Education',
    'description': """The learning management (LSM) Application is a 
    web-based platform designed to manage online educational courses.""",
    
    'depends' : ['website','base','mail'],
    'data': [
        'security/lms_security.xml',
        'security/ir.model.access.csv',
        'views/lms_assignment_view.xml',
        'wizard/lms_wizard_view.xml',
        'views/lms_enrollment_view.xml',
        'views/lms_course_types_view.xml',
        'views/lms_assignment_sub_view.xml',
        'views/lms_grade_view.xml',
        'views/template.xml',
        'views/res_user_view.xml',
        'views/lms_menu_view.xml',
        'report/enrollment_template.xml',
        'report/enrollment_report.xml',
    
    ],
    'demo' : [
        'demo/demo_course_types.xml',
        'demo/demo_assignments.xml',
        'demo/demo_enrollment.xml',
    ], 
    'installable': True,
    'application' : True,
}