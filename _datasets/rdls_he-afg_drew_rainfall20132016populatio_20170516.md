---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA TRMM mission
    url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: LandScan
    url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Gridded Population of the World (GPW v4)
    url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN OCHA
    url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
creator:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
dataset_id: rdls_he-afg_drew_rainfall20132016populatio_20170516
description: 'This report considers present and recent past food security assessments
  for Afghanistan in the context of hydrology, climate change and conflict. Population
  comparisons by data source (UN OCHA, LandScan, WorldPop, and Gridded Population
  of the World) and rainfall anomalies from 2013-2016 accompany the report. The authors,
  Zainab al Badri, Atia Curtiss, and Zoe Garcia, completed their research in partial
  fulfillment of Public Health coursework in Medical Geography, for Spring 2017, at
  Drew University. Dr. Lisa Jordan edited the report and supplemented their work with
  additional spatial data.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020]'
details: Model estimates made in the past tend not to account for recent demographic
  changes caused by conflict and displacement.
exposure:
- asset_type:
    description: Gridded population estimates from multiple sources (UN OCHA, LandScan,
      WorldPop, GPW v4) at sub-national level
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Rainfall anomalies were derived from satellite observations collected
    by the NASA TRMM mission for 2013-2016. Population data were compiled from four
    independent sources (UN OCHA, LandScan, WorldPop, GPW v4) using geospatial and
    remotely sensed modeling approaches. These datasets were integrated with food
    security assessments to synthesize relationships between hydroclimatic variability,
    population distribution, and food security outcomes in Afghanistan.
  sources:
  - id: source_1
    license: null
    name: NASA TRMM mission
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: LandScan
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: Gridded Population of the World (GPW v4)
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_5
    license: null
    name: UN OCHA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-rainfall-2013-2016-and-population-comparisons-2010-2020
  rel: source
loss: null
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
  description: 'A comparison of population estimates for Afghanistan provinces from
    four different sources: UN OCHA, LandScan, WorldPop, and Gridded Population of
    the World (GPW, version 4). Values are compared in a table in the attached food
    security and public health synthesis report.'
  download_url: https://data.humdata.org/dataset/f63eb6e8-8279-4f7e-88f6-5a8c6ed1739f/resource/b21605a9-fc4d-40c8-815e-55dab67d47a6/download/afg_adm1_populationcomparison.zip
  format: null
  id: resource_b21605a9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AFG_ADM1_PopulationComparison.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: TRMM global rain fall from NASA for March, 2000-2010 and 2013-2016.
    Data extracted for Afghanistan. Anomalies are identified by comparing mean and
    standard deviation (2000-2010) values to more recent measures (2013-2016). Areas
    one and two standard deviations above and below the mean are illustrated in the
    accompanying food security and public health synthesis reports. Metadata titled
    AFG_Rainfall are included in the Rainfall subfolder, and describes the many raster
    grids organized by year.
  download_url: https://data.humdata.org/dataset/f63eb6e8-8279-4f7e-88f6-5a8c6ed1739f/resource/014a1c7a-f38a-4078-84ae-9008c8c1bb4a/download/afg_rainfall.zip
  format: null
  id: resource_014a1c7a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AFG_Rainfall.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In the 'Food Security and Public Health Synthesis Report - Afghanistan,'
    Zainab al Badri, Atia Curtiss, and Zoe Garcia explore how climate, hydrology,
    and conflict impose limits to food availability in Afghanistan, and how conflict
    and returnees constrict economic opportunity and access to food.
  download_url: https://data.humdata.org/dataset/f63eb6e8-8279-4f7e-88f6-5a8c6ed1739f/resource/f004a8e3-3375-4688-8f7a-fd5ff8c4a6e3/download/food-security-and-public-health-synthesis-report-afghanistan-2017.pdf
  format: null
  id: resource_f004a8e3
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food Security and Public Health Synthesis Report - Afghanistan - 2017.pdf
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-afg_drew_rainfall20132016populatio_20170516
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-05-16'
temporal_resolution: null
title: 'Afghanistan Rainfall (2013-2016) and Population Comparisons (2010-2020): A
  Public Health and Food Security Synthesis Report with Corresponding Data'
version: null
vulnerability: null
---
