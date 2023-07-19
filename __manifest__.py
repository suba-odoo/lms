{
    'name': 'Learning management System',
    'version': '1.0',
    'category': 'Education',
    'description': """The learning management (LSM) Application is a 
    web-based platform designed to manage online educational courses.""",
    
    'depends' : ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/lms_views.xml',
        'views/lms_assignment_view.xml',
        'views/lms_enrollment_view.xml',
        'views/lms_course_types_view.xml',
        'views/lms_assignment_sub_view.xml',
        'views/lms_grade_view.xml',
        'views/lms_menu_view.xml',
        'report/enrollment_template.xml',
        'report/enrollment_report.xml',
    
    ],
    'demo' : [
        'demo/demo.xml',
        'demo/demo_course_types.xml',
        'demo/demo_assignments.xml',
    ], 
    'installable': True,
    'application' : True,
}