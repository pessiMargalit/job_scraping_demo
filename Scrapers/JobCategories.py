import enum
from difflib import SequenceMatcher


class JobCategories(enum.Enum):
    content = "Content"
    data_and_analytics = "Data & Analytics"
    design_and_ux = "Design & UX"
    dev_and_engineer = "Dev & Engineer"
    finance = "Finance"
    hr_and_recruiting = "HR & Recruiting"
    internships = "Internships"
    legal = "Legal"
    marketing = "Marketing"
    operations = "Operations"
    product = "Product"
    project_management = "Project Management"
    sales = "Sales"

    @staticmethod
    def subcategory(category):
        return {
            JobCategories.content.value: [],
            JobCategories.data_and_analytics.value: [
                'Analytics',
                'Analysis & Reporting',
                'Business Intelligence',
                'Data Engineering',
                'Data Science',
                'Machine Learning',
                'Management',
                'Other'
            ],
            JobCategories.design_and_ux.value: [],
            JobCategories.dev_and_engineer.value: [
                'Android (Java)',
                'C++',
                'C#',
                'DevOps',
                'Front-End',
                'Golang',
                'Java',
                'Javascript',
                'Hardware',
                'iOS',
                'Linux',
                'Management',
                '.NET',
                'Perl',
                'PHP',
                'Python',
                'QA',
                'Ruby',
                'Salesforce',
                'Sales Engineer',
                'Scala'
                'Security',
                'Other'
            ],
            JobCategories.finance.value: [],
            JobCategories.hr_and_recruiting.value: [],
            JobCategories.internships.value: [],
            JobCategories.legal.value: [],
            JobCategories.marketing.value: [],
            JobCategories.operations.value: [
                'Client Success',
                'Customer Support',
                'IT',
                'Office Management',
                'Operations Management',
                'Technical Support',
                'Other'
            ],
            JobCategories.product.value: [],
            JobCategories.project_management.value: [],
            JobCategories.sales.value: [
                'Account Executive',
                'Account Management',
                'Customer Success',
                'Leadership',
                'Operations',
                'Sales Development',
                'Sales Engineer'
            ]
        }[category]

    @staticmethod
    def similar(title):
        matches = []
        for sub_title in JobCategories.props(JobCategories):
            ratio_to_category = SequenceMatcher(None, title, sub_title.lower()).ratio()
            matches.append({'title': sub_title, 'ratio': ratio_to_category})
            if ratio_to_category > 0.4:
                for sub_category in JobCategories.subcategory(sub_title):
                    matches.append({'title': sub_category, 'ratio': SequenceMatcher(None, title, sub_category.lower()).ratio()})
        return sorted(matches, key=lambda m: m['ratio'], reverse=True)

    @staticmethod
    def props(cls):
        return [e.value for e in cls]