#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on April 01, 2020, at 17:24
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Attention and Perception\\project-2\\experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome to the experiment.\n\n1. Please look at the central box. \n2. Respond to the target as quickly as possible by pressing the space key.  ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# Initialize components for Routine "StartScreen"
StartScreenClock = core.Clock()
textStart = visual.TextStim(win=win, name='textStart',
    text="Let's start the experiment. \n\nPress space to begin.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyStart = keyboard.Keyboard()

# Initialize components for Routine "TrialScreenBefore"
TrialScreenBeforeClock = core.Clock()
imageTrailBefore_1 = visual.ImageStim(
    win=win,
    name='imageTrailBefore_1', 
    image='images/light_grey_box', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=256, interpolate=True, depth=0.0)
imageTrialBefore_2 = visual.ImageStim(
    win=win,
    name='imageTrialBefore_2', 
    image='images/light_grey_box', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageTrialBefore_3 = visual.ImageStim(
    win=win,
    name='imageTrialBefore_3', 
    image='images/light_grey_box', mask=None,
    ori=0, pos=(0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "TrialScreenCue"
TrialScreenCueClock = core.Clock()
imageTrialCue_1 = visual.ImageStim(
    win=win,
    name='imageTrialCue_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageTrialCue_2 = visual.ImageStim(
    win=win,
    name='imageTrialCue_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageTrialCue_3 = visual.ImageStim(
    win=win,
    name='imageTrialCue_3', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "TrialSceenTarget"
TrialSceenTargetClock = core.Clock()
imageTrialTarget_1 = visual.ImageStim(
    win=win,
    name='imageTrialTarget_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imageTrialTarget_2 = visual.ImageStim(
    win=win,
    name='imageTrialTarget_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageTrialTarget_3 = visual.ImageStim(
    win=win,
    name='imageTrialTarget_3', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
keyResponse = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
textEndSceen = visual.TextStim(win=win, name='textEndSceen',
    text='Thank you for participating. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [textWelcome, keyWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space', 'enter'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyStart.keys = []
keyStart.rt = []
_keyStart_allKeys = []
# keep track of which components have finished
StartScreenComponents = [textStart, keyStart]
for thisComponent in StartScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartScreen"-------
while continueRoutine:
    # get current time
    t = StartScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textStart* updates
    if textStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textStart.frameNStart = frameN  # exact frame index
        textStart.tStart = t  # local t and not account for scr refresh
        textStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textStart, 'tStartRefresh')  # time at next scr refresh
        textStart.setAutoDraw(True)
    
    # *keyStart* updates
    waitOnFlip = False
    if keyStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyStart.frameNStart = frameN  # exact frame index
        keyStart.tStart = t  # local t and not account for scr refresh
        keyStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyStart, 'tStartRefresh')  # time at next scr refresh
        keyStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyStart.status == STARTED and not waitOnFlip:
        theseKeys = keyStart.getKeys(keyList=['space'], waitRelease=False)
        _keyStart_allKeys.extend(theseKeys)
        if len(_keyStart_allKeys):
            keyStart.keys = _keyStart_allKeys[-1].name  # just the last key pressed
            keyStart.rt = _keyStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartScreen"-------
for thisComponent in StartScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textStart.started', textStart.tStartRefresh)
thisExp.addData('textStart.stopped', textStart.tStopRefresh)
# check responses
if keyStart.keys in ['', [], None]:  # No response was made
    keyStart.keys = None
thisExp.addData('keyStart.keys',keyStart.keys)
if keyStart.keys != None:  # we had a response
    thisExp.addData('keyStart.rt', keyStart.rt)
thisExp.addData('keyStart.started', keyStart.tStartRefresh)
thisExp.addData('keyStart.stopped', keyStart.tStopRefresh)
thisExp.nextEntry()
# the Routine "StartScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimuli.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TrialScreenBefore"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    TrialScreenBeforeComponents = [imageTrailBefore_1, imageTrialBefore_2, imageTrialBefore_3]
    for thisComponent in TrialScreenBeforeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialScreenBeforeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrialScreenBefore"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialScreenBeforeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialScreenBeforeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTrailBefore_1* updates
        if imageTrailBefore_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrailBefore_1.frameNStart = frameN  # exact frame index
            imageTrailBefore_1.tStart = t  # local t and not account for scr refresh
            imageTrailBefore_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrailBefore_1, 'tStartRefresh')  # time at next scr refresh
            imageTrailBefore_1.setAutoDraw(True)
        if imageTrailBefore_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrailBefore_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                imageTrailBefore_1.tStop = t  # not accounting for scr refresh
                imageTrailBefore_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrailBefore_1, 'tStopRefresh')  # time at next scr refresh
                imageTrailBefore_1.setAutoDraw(False)
        
        # *imageTrialBefore_2* updates
        if imageTrialBefore_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrialBefore_2.frameNStart = frameN  # exact frame index
            imageTrialBefore_2.tStart = t  # local t and not account for scr refresh
            imageTrialBefore_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialBefore_2, 'tStartRefresh')  # time at next scr refresh
            imageTrialBefore_2.setAutoDraw(True)
        if imageTrialBefore_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialBefore_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialBefore_2.tStop = t  # not accounting for scr refresh
                imageTrialBefore_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialBefore_2, 'tStopRefresh')  # time at next scr refresh
                imageTrialBefore_2.setAutoDraw(False)
        
        # *imageTrialBefore_3* updates
        if imageTrialBefore_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrialBefore_3.frameNStart = frameN  # exact frame index
            imageTrialBefore_3.tStart = t  # local t and not account for scr refresh
            imageTrialBefore_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialBefore_3, 'tStartRefresh')  # time at next scr refresh
            imageTrialBefore_3.setAutoDraw(True)
        if imageTrialBefore_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialBefore_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialBefore_3.tStop = t  # not accounting for scr refresh
                imageTrialBefore_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialBefore_3, 'tStopRefresh')  # time at next scr refresh
                imageTrialBefore_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialScreenBeforeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrialScreenBefore"-------
    for thisComponent in TrialScreenBeforeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('imageTrailBefore_1.started', imageTrailBefore_1.tStartRefresh)
    trials.addData('imageTrailBefore_1.stopped', imageTrailBefore_1.tStopRefresh)
    trials.addData('imageTrialBefore_2.started', imageTrialBefore_2.tStartRefresh)
    trials.addData('imageTrialBefore_2.stopped', imageTrialBefore_2.tStopRefresh)
    trials.addData('imageTrialBefore_3.started', imageTrialBefore_3.tStartRefresh)
    trials.addData('imageTrialBefore_3.stopped', imageTrialBefore_3.tStopRefresh)
    
    # ------Prepare to start Routine "TrialScreenCue"-------
    continueRoutine = True
    routineTimer.add(0.150000)
    # update component parameters for each repeat
    imageTrialCue_1.setImage(image_cue_1)
    imageTrialCue_2.setImage(image_cue_2)
    imageTrialCue_3.setImage(image_cue_3)
    # keep track of which components have finished
    TrialScreenCueComponents = [imageTrialCue_1, imageTrialCue_2, imageTrialCue_3]
    for thisComponent in TrialScreenCueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialScreenCueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrialScreenCue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialScreenCueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialScreenCueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTrialCue_1* updates
        if imageTrialCue_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrialCue_1.frameNStart = frameN  # exact frame index
            imageTrialCue_1.tStart = t  # local t and not account for scr refresh
            imageTrialCue_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialCue_1, 'tStartRefresh')  # time at next scr refresh
            imageTrialCue_1.setAutoDraw(True)
        if imageTrialCue_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialCue_1.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialCue_1.tStop = t  # not accounting for scr refresh
                imageTrialCue_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialCue_1, 'tStopRefresh')  # time at next scr refresh
                imageTrialCue_1.setAutoDraw(False)
        
        # *imageTrialCue_2* updates
        if imageTrialCue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrialCue_2.frameNStart = frameN  # exact frame index
            imageTrialCue_2.tStart = t  # local t and not account for scr refresh
            imageTrialCue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialCue_2, 'tStartRefresh')  # time at next scr refresh
            imageTrialCue_2.setAutoDraw(True)
        if imageTrialCue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialCue_2.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialCue_2.tStop = t  # not accounting for scr refresh
                imageTrialCue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialCue_2, 'tStopRefresh')  # time at next scr refresh
                imageTrialCue_2.setAutoDraw(False)
        
        # *imageTrialCue_3* updates
        if imageTrialCue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrialCue_3.frameNStart = frameN  # exact frame index
            imageTrialCue_3.tStart = t  # local t and not account for scr refresh
            imageTrialCue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialCue_3, 'tStartRefresh')  # time at next scr refresh
            imageTrialCue_3.setAutoDraw(True)
        if imageTrialCue_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialCue_3.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialCue_3.tStop = t  # not accounting for scr refresh
                imageTrialCue_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialCue_3, 'tStopRefresh')  # time at next scr refresh
                imageTrialCue_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialScreenCueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrialScreenCue"-------
    for thisComponent in TrialScreenCueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('imageTrialCue_1.started', imageTrialCue_1.tStartRefresh)
    trials.addData('imageTrialCue_1.stopped', imageTrialCue_1.tStopRefresh)
    trials.addData('imageTrialCue_2.started', imageTrialCue_2.tStartRefresh)
    trials.addData('imageTrialCue_2.stopped', imageTrialCue_2.tStopRefresh)
    trials.addData('imageTrialCue_3.started', imageTrialCue_3.tStartRefresh)
    trials.addData('imageTrialCue_3.stopped', imageTrialCue_3.tStopRefresh)
    
    # ------Prepare to start Routine "TrialSceenTarget"-------
    continueRoutine = True
    # update component parameters for each repeat
    imageTrialTarget_1.setImage(image_target_1)
    imageTrialTarget_2.setImage(image_target_2)
    imageTrialTarget_3.setImage(image_target_3)
    keyResponse.keys = []
    keyResponse.rt = []
    _keyResponse_allKeys = []
    # keep track of which components have finished
    TrialSceenTargetComponents = [imageTrialTarget_1, imageTrialTarget_2, imageTrialTarget_3, keyResponse]
    for thisComponent in TrialSceenTargetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialSceenTargetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TrialSceenTarget"-------
    while continueRoutine:
        # get current time
        t = TrialSceenTargetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialSceenTargetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTrialTarget_1* updates
        if imageTrialTarget_1.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            imageTrialTarget_1.frameNStart = frameN  # exact frame index
            imageTrialTarget_1.tStart = t  # local t and not account for scr refresh
            imageTrialTarget_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialTarget_1, 'tStartRefresh')  # time at next scr refresh
            imageTrialTarget_1.setAutoDraw(True)
        if imageTrialTarget_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialTarget_1.tStartRefresh + 0.20-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialTarget_1.tStop = t  # not accounting for scr refresh
                imageTrialTarget_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialTarget_1, 'tStopRefresh')  # time at next scr refresh
                imageTrialTarget_1.setAutoDraw(False)
        
        # *imageTrialTarget_2* updates
        if imageTrialTarget_2.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            imageTrialTarget_2.frameNStart = frameN  # exact frame index
            imageTrialTarget_2.tStart = t  # local t and not account for scr refresh
            imageTrialTarget_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialTarget_2, 'tStartRefresh')  # time at next scr refresh
            imageTrialTarget_2.setAutoDraw(True)
        if imageTrialTarget_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialTarget_2.tStartRefresh + 0.20-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialTarget_2.tStop = t  # not accounting for scr refresh
                imageTrialTarget_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialTarget_2, 'tStopRefresh')  # time at next scr refresh
                imageTrialTarget_2.setAutoDraw(False)
        
        # *imageTrialTarget_3* updates
        if imageTrialTarget_3.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            imageTrialTarget_3.frameNStart = frameN  # exact frame index
            imageTrialTarget_3.tStart = t  # local t and not account for scr refresh
            imageTrialTarget_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrialTarget_3, 'tStartRefresh')  # time at next scr refresh
            imageTrialTarget_3.setAutoDraw(True)
        if imageTrialTarget_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrialTarget_3.tStartRefresh + 0.20-frameTolerance:
                # keep track of stop time/frame for later
                imageTrialTarget_3.tStop = t  # not accounting for scr refresh
                imageTrialTarget_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrialTarget_3, 'tStopRefresh')  # time at next scr refresh
                imageTrialTarget_3.setAutoDraw(False)
        
        # *keyResponse* updates
        waitOnFlip = False
        if keyResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyResponse.frameNStart = frameN  # exact frame index
            keyResponse.tStart = t  # local t and not account for scr refresh
            keyResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResponse, 'tStartRefresh')  # time at next scr refresh
            keyResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResponse.status == STARTED and not waitOnFlip:
            theseKeys = keyResponse.getKeys(keyList=None, waitRelease=False)
            _keyResponse_allKeys.extend(theseKeys)
            if len(_keyResponse_allKeys):
                keyResponse.keys = _keyResponse_allKeys[-1].name  # just the last key pressed
                keyResponse.rt = _keyResponse_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialSceenTargetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TrialSceenTarget"-------
    for thisComponent in TrialSceenTargetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('imageTrialTarget_1.started', imageTrialTarget_1.tStartRefresh)
    trials.addData('imageTrialTarget_1.stopped', imageTrialTarget_1.tStopRefresh)
    trials.addData('imageTrialTarget_2.started', imageTrialTarget_2.tStartRefresh)
    trials.addData('imageTrialTarget_2.stopped', imageTrialTarget_2.tStopRefresh)
    trials.addData('imageTrialTarget_3.started', imageTrialTarget_3.tStartRefresh)
    trials.addData('imageTrialTarget_3.stopped', imageTrialTarget_3.tStopRefresh)
    # check responses
    if keyResponse.keys in ['', [], None]:  # No response was made
        keyResponse.keys = None
    trials.addData('keyResponse.keys',keyResponse.keys)
    if keyResponse.keys != None:  # we had a response
        trials.addData('keyResponse.rt', keyResponse.rt)
    trials.addData('keyResponse.started', keyResponse.tStartRefresh)
    trials.addData('keyResponse.stopped', keyResponse.tStopRefresh)
    # the Routine "TrialSceenTarget" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank500Components = [textBlank500]
    for thisComponent in Blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank500* updates
        if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank500.frameNStart = frameN  # exact frame index
            textBlank500.tStart = t  # local t and not account for scr refresh
            textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(True)
        if textBlank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank500.tStop = t  # not accounting for scr refresh
                textBlank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
                textBlank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank500"-------
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textBlank500.started', textBlank500.tStartRefresh)
    trials.addData('textBlank500.stopped', textBlank500.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [textEndSceen]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndSceen* updates
    if textEndSceen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndSceen.frameNStart = frameN  # exact frame index
        textEndSceen.tStart = t  # local t and not account for scr refresh
        textEndSceen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndSceen, 'tStartRefresh')  # time at next scr refresh
        textEndSceen.setAutoDraw(True)
    if textEndSceen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndSceen.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndSceen.tStop = t  # not accounting for scr refresh
            textEndSceen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndSceen, 'tStopRefresh')  # time at next scr refresh
            textEndSceen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEndSceen.started', textEndSceen.tStartRefresh)
thisExp.addData('textEndSceen.stopped', textEndSceen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
