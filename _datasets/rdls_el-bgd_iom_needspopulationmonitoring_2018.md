---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-bangladesh-needs-and-population-monitoring-npm-round-14-site-assessment
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-bangladesh-needs-and-population-monitoring-npm-round-14-site-assessment
dataset_id: rdls_el-bgd_iom_needspopulationmonitoring_2018
description: 'Following an outbreak of violence on 25 August 2017 in Rakhine State,
  Myanmar, a new massive influx of Rohingya refugees to Cox''s Bazar, Bangladesh started
  in late August 2017. Most of the Rohingya refugees settled in Ukhia and Teknaf Upazilas
  of Cox''s Bazar, a district bordering Myanmar identified as the main entry area
  for border crossings. This dataset presents the result of the NPM Round 14 Site
  Assessment exercise, which collected information related to the Rohingya refugee
  population distribution and needs during the months of December 2018 and January-February
  2019. The data collection for NPM baseline survey was conducted between 9 to 19
  December 2018: it provides an update about the population distribution and movements.
  The data collection for NPM Site Assessment survey was conducted between 14 January
  to 13 February 2019: in addition to an update about the population figures, this
  includes a multi-sectoral needs assessment. Rohingya refugee population distribution
  by para in Teknaf upazila. Please click here .. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/iom-bangladesh-needs-and-population-monitoring-npm-round-14-site-assessment]'
details: null
exposure:
- asset_type:
    description: Rohingya refugee population distribution across settlement sites
      in Cox's Bazar
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM conducted direct observational site assessments across Rohingya
    refugee settlements in Cox's Bazar following the August 2017 influx from Myanmar.
    Data collection involved field surveys documenting population distribution and
    humanitarian needs (shelter, WASH, health, food security) across settlement sites
    in Ukhia and Teknaf Upazilas during December 2018 and January-February 2019.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iom-bangladesh-needs-and-population-monitoring-npm-round-14-site-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Rohingya refugee population needs assessment including shelter, WASH,
      and health vulnerabilities
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
        metric: exposure
        modelling: observed
        type: total
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
  description: IOM Bangladesh - Needs and Population Monitoring (NPM) Round 14 Site
    Assessment (Excel)
  download_url: https://data.humdata.org/dataset/f65ae171-6a8a-431e-8caf-37ab33654fed/resource/91d85440-8758-46b8-8e74-7edfa37e5d33/download/npm-site-assessment-round-14-dataset-20190213.xlsx
  format: null
  id: resource_91d85440
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npm-site-assessment-round-14-dataset-20190213.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Bangladesh - Needs and Population Monitoring (NPM) Round 14 Site
    Assessment (IOM Bangladesh NPM Methodology - December 2018.pdf)
  download_url: https://data.humdata.org/dataset/f65ae171-6a8a-431e-8caf-37ab33654fed/resource/3e3d8831-ec3c-474d-a273-9fd1a52890a2/download/iom-bangladesh-npm-methodology-december-2018.pdf
  format: null
  id: resource_3e3d8831
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IOM Bangladesh NPM Methodology - December 2018.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_iom_needspopulationmonitoring_2018
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
  end: '2019-02-13'
  start: '2018-12-09'
temporal_resolution: null
title: IOM Bangladesh - Needs and Population Monitoring (NPM) Round 14 Site Assessment
version: null
vulnerability: null
---
