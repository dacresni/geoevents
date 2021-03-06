# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Billet'
        db.create_table(u'director_billet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('date_open', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_advertised', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_filled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_expires', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_vacant', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_extension', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_review', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_selected', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('dept', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('org', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('band_level', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('selectee', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('aon_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'director', ['Billet'])

        # Adding M2M table for field director_billets on 'DirectorDashboard'
        db.create_table(u'director_directordashboard_director_billets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('directordashboard', models.ForeignKey(orm[u'director.directordashboard'], null=False)),
            ('billet', models.ForeignKey(orm[u'director.billet'], null=False))
        ))
        db.create_unique(u'director_directordashboard_director_billets', ['directordashboard_id', 'billet_id'])


    def backwards(self, orm):
        
        # Deleting model 'Billet'
        db.delete_table(u'director_billet')

        # Removing M2M table for field director_billets on 'DirectorDashboard'
        db.delete_table('director_directordashboard_director_billets')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 21, 14, 9, 26, 252504)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 21, 14, 9, 26, 251719)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'director.billet': {
            'Meta': {'object_name': 'Billet'},
            'aon_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'band_level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_advertised': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_extension': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_filled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_open': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_review': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_selected': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_vacant': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'org': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'selectee': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        u'director.dashboardwidgets': {
            'Meta': {'ordering': "['order']", 'object_name': 'DashboardWidgets'},
            'dashboard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['director.DirectorDashboard']"}),
            'data_json_org': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '250', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['director.PageWidget']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '6', 'max_length': '2'})
        },
        u'director.directordashboard': {
            'Meta': {'ordering': "['org']", 'object_name': 'DirectorDashboard'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'director_billets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.Billet']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'org': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '250', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'page_widgets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.PageWidget']", 'null': 'True', 'through': u"orm['director.DashboardWidgets']", 'blank': 'True'}),
            'related_links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.Link']", 'null': 'True', 'blank': 'True'}),
            'related_program_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.ProgramGroup']", 'null': 'True', 'blank': 'True'}),
            'site_icon': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'tracking_code': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Portal'", 'max_length': '10'})
        },
        u'director.link': {
            'Meta': {'ordering': "['category', 'rating_count', 'title']", 'object_name': 'Link'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'Links'", 'max_length': '60'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1000'}),
            'technical_poc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'director.pagewidget': {
            'Meta': {'ordering': "['name']", 'object_name': 'PageWidget'},
            'data_json': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iframe_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'iframe_url_if_local': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'render_function': ('django.db.models.fields.CharField', [], {'default': "'notesAndChildNotes'", 'max_length': '60'}),
            'subtext': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'Thick'", 'max_length': '15'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Wiki'", 'max_length': '10'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'director.programgroup': {
            'Meta': {'ordering': "['name', 'tags']", 'object_name': 'ProgramGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'related_links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.Link']", 'null': 'True', 'blank': 'True'}),
            'related_programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.ProgramInfo']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'director.programinfo': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProgramInfo'},
            'contract_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contractor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'government_cor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'government_cotr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'government_pm': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'period_of_performance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'director.programobservation': {
            'Meta': {'ordering': "['-observation_entered']", 'object_name': 'ProgramObservation'},
            'budget_cost': ('django.db.models.fields.TextField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'classification': ('django.db.models.fields.CharField', [], {'default': "'UNCLASSIFIED'", 'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entered_by': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '250', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'execution_cost': ('django.db.models.fields.TextField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'funds_cost': ('django.db.models.fields.TextField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issues_performance': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'metric_cost': ('django.db.models.fields.CharField', [], {'default': "'Yellow'", 'max_length': '10'}),
            'metric_overall': ('django.db.models.fields.CharField', [], {'default': "'Yellow'", 'max_length': '10'}),
            'metric_performance': ('django.db.models.fields.CharField', [], {'default': "'Yellow'", 'max_length': '10'}),
            'metric_schedule': ('django.db.models.fields.CharField', [], {'default': "'Yellow'", 'max_length': '10'}),
            'observation_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'pm_observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['director.ProgramInfo']"}),
            'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1000'}),
            'risk_performance': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_cost': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_overall': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_performance': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_schedule': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'trend_cost': ('django.db.models.fields.CharField', [], {'default': "'Middle'", 'max_length': '10'}),
            'trend_overall': ('django.db.models.fields.CharField', [], {'default': "'Middle'", 'max_length': '10'}),
            'trend_performance': ('django.db.models.fields.CharField', [], {'default': "'Middle'", 'max_length': '10'}),
            'trend_schedule': ('django.db.models.fields.CharField', [], {'default': "'Middle'", 'max_length': '10'})
        },
        u'director.report': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Report'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '250', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '1000'}),
            'related_boards': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.DirectorDashboard']", 'null': 'True', 'blank': 'True'}),
            'related_links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.Link']", 'null': 'True', 'blank': 'True'}),
            'related_programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['director.ProgramInfo']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['director']
