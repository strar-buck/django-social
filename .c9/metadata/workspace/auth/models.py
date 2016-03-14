{"filter":false,"title":"models.py","tooltip":"/auth/models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":4,"column":0},"end":{"row":4,"column":26},"action":"remove","lines":["# Create your models here."],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":28},"action":"remove","lines":["from __future__ import unicode_literals","","from django.db import models"],"id":3},{"start":{"row":0,"column":0},"end":{"row":129,"column":0},"action":"insert","lines":["from django.contrib.auth.models import User","from django.db.models.signals import post_save","from django.db import models","from django.conf import settings","import os.path","from active.models import Notification","import urllib, hashlib","","class Profile(models.Model):","    user = models.OneToOneField(User)","    location = models.CharField(max_length=50, null=True, blank=True)","    url = models.CharField(max_length=50, null=True, blank=True)","    job_title = models.CharField(max_length=50, null=True, blank=True)","    #reputation = models.IntegerField(default=0)","    #language = models.CharField(max_length=5, default='en')","","","    def get_url(self):","        url = self.url","        if \"http://\" not in self.url and \"https://\" not in self.url and len(self.url) > 0:","            url = \"http://\" + str(self.url)","        return url ","","    def get_picture(self):","        no_picture = 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTIH-l2Mqzxu-gm4M6R0zFzizYeKkMdw3YJL02FORmQXDOmIX4ZS7u5lA'","        try:","            filename = settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'","            picture_url = settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'","            if os.path.isfile(filename):","                return picture_url","            else:","                gravatar_url = u'http://www.gravatar.com/avatar/{0}?{1}'.format(","                    hashlib.md5(self.user.email.lower()).hexdigest(),","                    urllib.urlencode({'d':no_picture, 's':'256'})","                    )","                return gravatar_url","        except Exception, e:","            return no_picture","","    def get_screen_name(self):","        try:","            if self.user.get_full_name():","                return self.user.get_full_name()","            else:","                return self.user.username","        except:","            return self.user.username","","    '''def notify_liked(self, feed):","        if self.user != feed.user:","            print feed","            print '%s has liked %s ' % (self.user,feed.user)","            print self","            Notification(notification_type=Notification.LIKED,","                from_user=self.user,","                to_user=feed.user,","                feed=feed).save()","","    def unotify_liked(self, feed):","        if self.user != feed.user:","            Notification.objects.filter(notification_type=Notification.LIKED,","                from_user=self.user, ","                to_user=feed.user, ","                feed=feed).delete()","","    def notify_commented(self, feed):","        if self.user != feed.user:","            Notification(notification_type=Notification.COMMENTED,","                        from_user=self.user,","                        to_user=feed.user,","                        feed=feed).save()","","    def notify_also_commented(self, feed):","        comments = feed.get_comments()","        users = []","        for comment in comments:","            if comment.user != self.user and comment.user != feed.user:","                users.append(comment.user.pk)","        users = list(set(users))","        for user in users:","            Notification(notification_type=Notification.ALSO_COMMENTED,","                from_user=self.user,","                to_user=User(id=user),","                feed=feed).save()","","    def notify_favorited(self, question):","        if self.user != question.user:","            Notification(notification_type=Notification.FAVORITED,","                from_user=self.user, ","                to_user=question.user, ","                question=question).save()","","    def unotify_favorited(self, question):","        if self.user != question.user:","            Notification.objects.filter(notification_type=Notification.FAVORITED,","                from_user=self.user, ","                to_user=question.user, ","                question=question).delete()","","    def notify_answered(self, question):","        if self.user != question.user:","            Notification(notification_type=Notification.ANSWERED,","                from_user=self.user, ","                to_user=question.user, ","                question=question).save()","    ","    def notify_accepted(self, answer):","        if self.user != answer.user:","            Notification(notification_type=Notification.ACCEPTED_ANSWER,","                from_user=self.user, ","                to_user=answer.user, ","                answer=answer).save()","    ","    def unotify_accepted(self, answer):","        if self.user != answer.user:","            Notification.objects.filter(notification_type=Notification.ACCEPTED_ANSWER,","                from_user=self.user, ","                to_user=answer.user, ","                answer=answer).delete()'''","","def create_user_profile(sender, instance, created, **kwargs):","    if created:","        Profile.objects.create(user=instance)","","def save_user_profile(sender, instance, **kwargs):","    instance.profile.save()","","post_save.connect(create_user_profile, sender=User)","post_save.connect(save_user_profile, sender=User)",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1456490881885,"hash":"2bf4b69ff7c336b0638daaa19070256eaa3603e9"}