import getpass
from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event, Profile, Team, Contestant
from zestpkg.event.utils import *
from math import ceil