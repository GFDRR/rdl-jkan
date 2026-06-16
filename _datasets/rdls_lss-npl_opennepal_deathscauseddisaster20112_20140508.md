---
attributions:
- entity:
    affiliation: null
    email: null
    name: Nepal Disaster Report 2013
    url: https://data.humdata.org/dataset/deaths-caused-by-disaster-2011-2012
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/deaths-caused-by-disaster-2011-2012
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/deaths-caused-by-disaster-2011-2012
dataset_id: rdls_lss-npl_opennepal_deathscauseddisaster20112_20140508
description: 'This file include no of death caused by disaster, according to their
  region in 2011 and 2012. It was extracted from Nepal disaster Report 2013 which
  was published by Ministry of Home and Affair. Link : http://www.moha.gov.np//uploads/publications/file/Nepal%20Disaster%20Rep....
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/deaths-caused-by-disaster-2011-2012]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Post-event mortality data extracted from the official Nepal Disaster
    Report 2013 published by the Ministry of Home Affairs, aggregating deaths caused
    by natural disasters by administrative region for the years 2011-2012.
  sources:
  - id: source_1
    license: null
    name: Nepal Disaster Report 2013
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/deaths-caused-by-disaster-2011-2012
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Deaths caused by disasters (primarily earthquake) by region in Nepal
      2011-2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Deaths caused by disasters (primarily flood) by region in Nepal 2011-2012
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths caused by disasters (primarily landslide) by region in Nepal
      2011-2012
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Deaths caused by disaster ,2011-2012 (Deaths%20caused%20by%20disaster.csv)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/Deaths%20caused%20by%20disaster.csv&nid=2544
  format: null
  id: resource_a808140c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Deaths%20caused%20by%20disaster.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_deathscauseddisaster20112_20140508
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-05-08'
temporal_resolution: null
title: Nepal - Deaths caused by disaster ,2011-2012
version: null
vulnerability: null
---
