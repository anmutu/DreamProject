# _*_ coding:utf-8 _*_
__author__ = 'Ando'
__date__ = '7/7/2017 11:06 AM'

import xadmin

from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse


class UserAskAdmin(object):
    pass


class CourseCommentsAdmin(object):
    pass


class UserFavoriteAdmin(object):
    pass


class UserMessageAdmin(object):
    pass


class UserCourseAdmin(object):
    pass


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserFavoriteAdmin)