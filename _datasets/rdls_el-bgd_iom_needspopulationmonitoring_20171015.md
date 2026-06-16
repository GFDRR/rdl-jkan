---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Needs and Population Monitoring
      (NPM)
    url: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-round-6-for-rohingya-population-in-cox-s-bazar-district
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-round-6-for-rohingya-population-in-cox-s-bazar-district
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-round-6-for-rohingya-population-in-cox-s-bazar-district
dataset_id: rdls_el-bgd_iom_needspopulationmonitoring_20171015
description: 'Following an outbreak of violence on 25 August 2017 in Rakhine State,
  Myanmar, a new massive influx of Rohingya refugees to Cox''s Bazar, Bangladesh started
  in late August 2017. Most of the Rohingya refugees settled in Ukhia and Teknaf Upazilas
  of Cox''s Bazar, a district bordering Myanmar identified as the main entry area
  for border crossings. This assessment covers all locations hosting Rohingya population
  in Cox''s Bazar District in Bangladesh and present needs overview and population
  information as of 15 October 2017. All information and findings are included in
  the attached products including the raw dataset for further reference and analysis.
  Full report available on humanitarianresponse.info. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-round-6-for-rohingya-population-in-cox-s-bazar-district]'
details: A total of 28 Collective Sites and 99 Locations with dispersed setting in
  host communities were assessed between 30 September - 9 October 2017. Total of 794,658
  Rohingyas were identified in Cox's Bazar District. This figure has also taken into
  consideration additional figures collected on a daily basis through NPM Emergency
  Tracking - Flow Monitoring exercise up to 15 October 2017 and other relevant secondary
  data sources available. The finding estimates over 582,000 New Arrivals have arrived
  since 25 August 2017.
exposure:
- asset_type:
    description: Rohingya refugee population enumerated by site and household in Cox's
      Bazar District
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Direct field observation and enumeration of Rohingya refugee populations
    across all settlement sites in Cox's Bazar District, Bangladesh, conducted by
    IOM as of 15 October 2017. Site-level data on households and individuals were
    collected through anecdotal/observational methods and compiled into a spatial
    geodataset with administrative boundaries and site locations to document displacement
    impacts and population distribution.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Needs and Population Monitoring
      (NPM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-round-6-for-rohingya-population-in-cox-s-bazar-district
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Rohingya population displaced by violence in Rakhine State, Myanmar,
      now residing in refugee sites in Bangladesh
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
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
  description: Needs and Population Monitoring (NPM) Round 6. This assessment covers
    all locations hosting Rohingya population in Cox's Bazar District in Bangladesh
    and present needs overview and population information as of 15 Oct. All information
    and findings are included in the attached products including the raw dataset for
    further reference and analysis.
  download_url: https://data.humdata.org/dataset/49f3ad79-eaeb-4df0-8da2-007c0f25ff71/resource/97b168a9-0d88-4f42-b1da-18fd8ddc355e/download/npm-r6-site-assessment-dataset_2017-october.xlsx
  format: null
  id: resource_97b168a9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NPM-R6-Site-Assessment-Dataset_2017-October.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Bangladesh- Needs and Population Monitoring (NPM) Round 6 Site
    Assessment (Zipped shapefile containing data from the Master List tab of the Excel
    file)
  download_url: https://data.humdata.org/dataset/49f3ad79-eaeb-4df0-8da2-007c0f25ff71/resource/345fdc24-5122-4890-9390-e2149d64fedb/download/master_list.shp.zip
  format: null
  id: resource_345fdc24
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: master_list.shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_iom_needspopulationmonitoring_20171015
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-15'
temporal_resolution: null
title: IOM Bangladesh- Needs and Population Monitoring (NPM) Round 6 Site Assessment
version: null
vulnerability: null
---
