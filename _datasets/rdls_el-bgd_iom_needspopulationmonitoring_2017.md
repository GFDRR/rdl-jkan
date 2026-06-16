---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-bangladesh-round-8-site-assessment
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-bangladesh-round-8-site-assessment
dataset_id: rdls_el-bgd_iom_needspopulationmonitoring_2017
description: 'Following an outbreak of violence on 25 August 2017 in Rakhine State,
  Myanmar, a new massive influx of Rohingya refugees to Cox''s Bazar, Bangladesh started
  in late August 2017. Most of the Rohingya refugees settled in Ukhia and Teknaf Upazilas
  of Cox''s Bazar, a district bordering Myanmar identified as the main entry area
  for border crossings. This assessment presents data from NPM Round 8 baseline survey
  and site assessment: the baseline was conducted between 24 December 2017 and 4 January
  2018; the site assessment between 15 and 30 January 2018. The complete data collection
  was conducted between 24 December and 30 January 2018. For further information,
  the full report and related information package are available on humanitarianresponse.info.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-bangladesh-round-8-site-assessment]'
details: null
exposure:
- asset_type:
    description: Rohingya refugee population in Cox's Bazar camps assessed for needs
      and vulnerabilities
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
  description: IOM conducted direct observational surveys via baseline assessment
    (24 December 2017 - 4 January 2018) and site assessment (15-30 January 2018) of
    Rohingya refugee populations in Cox's Bazar following the August 2017 displacement
    crisis. Data collection documented population characteristics, needs, and camp
    conditions through structured site visits and interviews, producing two integrated
    datasets for humanitarian needs monitoring.
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
- href: https://data.humdata.org/dataset/needs-and-population-monitoring-npm-bangladesh-round-8-site-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Refugee population affected by displacement crisis with documented
      needs across shelter, water, sanitation, and health
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
  description: This dataset presents population numbers of Rohingya population in
    Cox's Bazar district as of 4 January 2018.
  download_url: https://data.humdata.org/dataset/2a44a78e-3990-44b0-889b-67a3cdd1f704/resource/167c8b37-08a8-46cf-aef8-0cd8eb3cd8c8/download/npm-r8-baseline-dataset_2018-03-08.xlsx
  format: null
  id: resource_167c8b37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NPM-R8-Baseline-Dataset_2018-01-04.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset presents population numbers of Rohingya population in
    Cox's Bazar district and needs assessment as of 30 January 2018.
  download_url: https://data.humdata.org/dataset/2a44a78e-3990-44b0-889b-67a3cdd1f704/resource/a896489a-831c-46ad-a43e-a601e683d995/download/npm-r8-site-assessment-dataset_2018-03-08.xlsx
  format: null
  id: resource_a896489a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NPM-R8-Site-Assessment-Dataset_2018-01-30.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Bangladesh - Needs and Population Monitoring (NPM) Round 8 Site
    Assessment (NPM Methodology - February 2018.pdf)
  download_url: https://data.humdata.org/dataset/2a44a78e-3990-44b0-889b-67a3cdd1f704/resource/a0a41e51-c22e-4ed2-aa2a-a2a2d664e593/download/npm-r8-full-methodology_2018-02-05.pdf
  format: null
  id: resource_a0a41e51
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NPM Methodology - February 2018.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_iom_needspopulationmonitoring_2017
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
  end: '2018-01-30'
  start: '2017-12-24'
temporal_resolution: null
title: IOM Bangladesh - Needs and Population Monitoring (NPM) Round 8 Site Assessment
version: null
vulnerability: null
---
