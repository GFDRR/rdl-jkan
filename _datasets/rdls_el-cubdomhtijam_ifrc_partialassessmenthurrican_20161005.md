---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Federation of Red Cross and Red Crescent Societies (IFRC)
      DCPPRR Americas Team
    url: https://data.humdata.org/dataset/partial-assessment-for-hurricane-matthew-as-of-05-10-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/partial-assessment-for-hurricane-matthew-as-of-05-10-2016
creator:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/partial-assessment-for-hurricane-matthew-as-of-05-10-2016
dataset_id: rdls_el-cubdomhtijam_ifrc_partialassessmenthurrican_20161005
description: 'Includes Assessment, two shapefiles: basemaps. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/partial-assessment-for-hurricane-matthew-as-of-05-10-2016]'
details: null
exposure:
- asset_type:
    description: Building stock affected by Hurricane Matthew
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population in areas affected by Hurricane Matthew
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage assessment data collected by IFRC through census-based
    3W/4W/5W methodology documenting building damage and affected populations from
    Hurricane Matthew. Data compiled into a consolidated assessment spreadsheet with
    geographic reference shapefiles for the Americas region.
  sources:
  - id: source_1
    license: null
    name: International Federation of Red Cross and Red Crescent Societies (IFRC)
      DCPPRR Americas Team
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/partial-assessment-for-hurricane-matthew-as-of-05-10-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Hurricane Matthew
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by Hurricane Matthew
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
        metric: exposure
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Partial assessment and 3 W's (Who, What,Where) as of 05/10/2015. only
    official information confimed has been included.
  download_url: https://drive.google.com/file/d/0B5OTV5P-3yL8ZDd6Yk5uZml1ZW8/view?usp=drive_web
  format: Google Sheet
  id: resource_b5fecfda
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Assessment_3W_05.10.2016_Hurricane_Matthew.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Partial Assessment for Hurricane Matthew (Countries in Americas)
  download_url: https://data.humdata.org/dataset/7ab8f4af-d867-49c4-af17-9fa7b625967b/resource/51b37019-fb35-4fda-b270-20b9c3dc713d/download/countriesamericas.shp.zip
  format: null
  id: resource_51b37019
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CountriesAmericas.shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cubdomhtijam_ifrc_partialassessmenthurrican_20161005
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  - DOM
  - CUB
  - JAM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-05'
temporal_resolution: null
title: Partial Assessment for Hurricane Matthew
version: null
vulnerability: null
---
