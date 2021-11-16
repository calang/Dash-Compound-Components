# Dash UI Compound Components (UICC)

Demonstration of how we can create compound Plotly Dash UI components
built as the combination of other components.

## Structure

![img.png](screenshot.png)

This app shows a layout with
* a rectangle showing a color gradient formed from 3 colors.
* three color mixers, each providing one of the colors used to 
  form the gradient

Each color mixer is composed of
* one color mix box, with the result of adding three
  primary color levels
* three color level panels, one for each primary color

Each color level panel is composed of
* one box showing a color level
* a knob, allowing adjustment of the color level

## Properties
The demo shows
### Composition
UICC-s can be created as a composition of other components.

### Nesting
UICC-s can be composed of simple UI components or other UICC-s.

### Addressability
Callbacks can be defined using
* attributes of components in a UICC, or
* attributes of components in a UICC within another UICC,  
  down to any desired level of nesting.

### Scalability
This approach proposes a way of 
organizing UI components in a scalable manner, from the program 
management point of view, making the code readable and more 
manageable, avoiding code duplication wherever possible. 

With respect to application performance, the approach uses component
and subcomponent ids made of strings, 
not dict-s, making the use of pattern-matching callbacks 
unnecessary.
This avoids the currently suggested limitation of 100+ callbacks 
 in 
[Dash 2.0 User's Guid - All-in-One Component Limitations](https://dash.plotly.com/all-in-one-components) section.

As with AIOC-s, the necessary callbacks are created without any 
duplicated code.

## Relationships with [All in One Components](https://dash.plotly.com/all-in-one-components) (AIOC-s)

The component interface functions that in UICC-s give 
access to internal component ids (those in `class ids`) is
compatible (has the same signature) with those in AIO Components.  
This give raise to the following possibilities.

1. AIOC-s can be nested within UICC-s
2. AIOC-s can be replaced with equivalent UICC-s that use the same 
   subcomponents, since their interface is the same; this assumes 
   there will be no use of embedded UICC subcomponents
3. UICC-s can also be implemented using pattern-matching callbacks,
   when found convenient.
   1. This might be the case when the UICC components to be 
      addressed by such callbacks don't involve nested components
   2. Convenience will depend on callback performance, among other 
      things.

## How to use
1. Clone this repo
   - `$ git clone __this_repo_url__`
2. Create an environment for your packages
   - `$ python -m venv venv`
3. Activate your environment
   - `$ source venv/bin/activate`
4. Add required packages
   - `$ pip install -r requirements.txt`
5. Run main.py
   - `venv/bin/python src/main.py`

## Requirements
* Python 3.8.10 or higher
* dash>=2.0
* dash-bootstrap-components
* dash_daq

## Credits
This approach is a derivation inspired on the
[Dash All-in-One Components](https://dash.plotly.com/all-in-one-components)
"convention for encapsulating layout and callbacks
into a reusable structure".

Past attempts at encapsulating Dash components that also 
contributed ideas are

1. [Dash Building Blocks](https://dash-building-blocks.readthedocs.io/en/latest/overview.html)
2. [Dash OOP Components](https://github.com/oegedijk/dash_oop_components)
3. [Composed Components](https://github.com/sdementen/dash-extensions/tree/composed-components#composed-components)

**Author**: carlos.a.lang@intel.com