---
attributions:
- entity:
    affiliation: null
    email: null
    name: The Migrants' Files
    url: https://data.humdata.org/dataset/refugee-and-migrant-deaths-while-trying-to-reach-europe
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Migrants' Files (inactive)
  url: https://data.humdata.org/dataset/refugee-and-migrant-deaths-while-trying-to-reach-europe
creator:
  affiliation: null
  email: null
  name: The Migrants' Files (inactive)
  url: https://data.humdata.org/dataset/refugee-and-migrant-deaths-while-trying-to-reach-europe
dataset_id: rdls_lss-tmf_refugeesmigrantdeathswhil_20151029
description: 'This dataset contains a list of events from 2000 to present during which
  someone died or went missing while trying to reach or stay in Europe. Details such
  as the date of the incident, the cause of death, number of dead and missing, location
  and coordinates of event are included.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/refugee-and-migrant-deaths-while-trying-to-reach-europe]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This dataset aggregates direct observational records of migration-related
    fatalities and missing persons incidents occurring during attempts to reach or
    remain in Europe. Data were collected through anecdotal reporting and compiled
    with incident-level details including date, location, cause of death, and casualty
    counts. The dataset serves as a historical record of disaster-related mortality
    impacts on migrant populations.
  sources:
  - id: source_1
    license: null
    name: The Migrants' Files
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/refugee-and-migrant-deaths-while-trying-to-reach-europe
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Deaths and missing persons during migration attempts across maritime
      routes to Europe
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths and missing persons during migration attempts across maritime
      routes to Europe
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
  description: Refugees and migrant deaths while trying to reach Europe (Events during
    which someone died trying to reach or stay in Europe)
  download_url: https://docs.google.com/spreadsheets/d/1YNqIzyQfEn4i_be2GGWESnG2Q80E_fLASffsXdCOftI/edit#gid=1085726718
  format: Google Sheet
  id: resource_cb5deda8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Events during which someone died trying to reach or stay in Europe
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CSV versions of the Events during which someone died trying to reach
    or stay in Europe google spreadsheet
  download_url: https://docs.google.com/spreadsheets/d/1YNqIzyQfEn4i_be2GGWESnG2Q80E_fLASffsXdCOftI/export?format=csv&id=1YNqIzyQfEn4i_be2GGWESnG2Q80E_fLASffsXdCOftI&gid=1085726718
  format: null
  id: resource_bea9c0fa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Events during which someone died trying to reach or stay in Europe.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zipped shapefile of events during which someone died trying to reach
    or stay in Europe
  download_url: https://data.humdata.org/dataset/82247dc0-c640-4e4d-9efd-0c139e4a59be/resource/e140d38a-ad4f-4e21-b58d-792b92a5b084/download/migrantfiles_casualties.zip
  format: null
  id: resource_e140d38a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: migrantfiles_casualties.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tmf_refugeesmigrantdeathswhil_20151029
spatial:
  bbox: null
  centroid: null
  countries:
  - GBR
  - ITA
  - GRC
  - ESP
  - FRA
  - TUR
  - LBY
  - TUN
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-29'
temporal_resolution: null
title: Refugees and migrant deaths while trying to reach Europe
version: null
vulnerability: null
---
