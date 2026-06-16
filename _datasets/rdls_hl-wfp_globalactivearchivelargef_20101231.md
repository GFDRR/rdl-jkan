---
attributions:
- entity:
    affiliation: null
    email: null
    name: Dartmouth Flood Observatory (DFO)
    url: https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
dataset_id: rdls_hl-wfp_globalactivearchivelargef_20101231
description: 'This data is from Darthmouth Flood Observatory (DFO) Global Active Archive
  of Large Flood Events. It contains more than 4000 records of flooding events globally
  from 1985 - 2010.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo]'
details: 'Please see this website for more information: http://floodobservatory.colorado.edu/Archives/index.html'
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: The Dartmouth Flood Observatory compiled a global archive of large
    flood events from 1985-2010 using direct observational data and anecdotal reports.
    Event records include spatial coordinates (centroid), temporal information (began/ended
    dates), and impact metrics (fatalities, displacement, economic damage). This dataset
    serves as an empirical inventory of observed flood impacts for global disaster
    risk assessment.
  sources:
  - id: source_1
    license: null
    name: Dartmouth Flood Observatory (DFO)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-active-archive-of-large-flood-events-dfo
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from observed flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced by observed flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic damage in USD from observed flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This data is from Darthmouth Flood Observatory (DFO) Global Active
    Archive of Large Flood Events. It contains more than 4000 records of flooding
    events globally from 1985 - 2010.
  download_url: https://data.humdata.org/dataset/1fd855de-57c6-42b3-83e1-9cf989b0f70d/resource/984cc240-b2b7-4266-9f61-5715a9e10ff5/download/wlf_nhr_fl_dfomasterlist_20190418.zip
  format: null
  id: resource_984cc240
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wlf_nhr_fl_dfomasterlist_20190418.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-wfp_globalactivearchivelargef_20101231
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2010-12-31'
temporal_resolution: null
title: Global Active Archive of Large Flood Events (DFO)
version: null
vulnerability: null
---
