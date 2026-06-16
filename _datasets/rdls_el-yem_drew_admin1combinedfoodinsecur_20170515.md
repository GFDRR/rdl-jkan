---
attributions:
- entity:
    affiliation: null
    email: null
    name: LandScan
    url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Gridded Population of the World version 4
    url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IPC Food Insecurity Phase Classification
    url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
creator:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
dataset_id: rdls_el-yem_drew_admin1combinedfoodinsecur_20170515
description: 'The data set includes the Admin1 boundaries and population estimates
  summarized from three sources as separate attributes: LandScan (2015), WorldPop
  (2010, 2015, and 2020), and Gridded Population of the World, version 4 (2015, 2020).
  The IPC Food Insecurity Phase Classification for Near and Medium Term (2017) are
  also included as attributes.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020]'
details: These data are derived from model estimates, and do not take recent displacement
  into account. Also, it should not be conflated that all residents within a food
  insecure area are experiencing food insecurity at the particular IPC phase. Particularly
  since the designations may be given, based on a proportion of the population experiencing
  a particular level of food insecurity.
exposure:
- asset_type:
    description: Modeled population estimates from LandScan, WorldPop, and GPW summarized
      by Admin1 boundaries
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
  description: Population estimates from three independent gridded population datasets
    (LandScan, WorldPop, GPW) were aggregated using zonal statistics within Admin1
    administrative boundaries. IPC Food Insecurity Phase classifications for 2017
    were integrated as loss attributes to characterize food security impacts at the
    subnational level.
  sources:
  - id: source_1
    license: null
    name: LandScan
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Gridded Population of the World version 4
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: IPC Food Insecurity Phase Classification
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/yemen-admin1-combined-food-insecurity-phase-2017-and-population-estimates-2015-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IPC Food Insecurity Phase Classification indicating population affected
      by food insecurity in 2017
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population Data according to multiple sources (LandScan, WorldPop,
    and GPW) for comparison by Food Insecurity severity (IPC Phase Classification),
    summarized by Admin1 boundaries (shapefile).
  download_url: https://data.humdata.org/dataset/90d299f0-da43-453b-b435-941df85da189/resource/bfb584ad-db7f-4b6b-9aff-825916584138/download/yemenadm1populationcomparison.zip
  format: null
  id: resource_bfb584ad
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: YemenAdm1PopulationComparison.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The document, 'Food Security and Public Health Synthesis Report,' written
    by Raza Hasanovic, Elizabeth Grein, and Abby Staskel, identifies connections between
    public health and food insecurity in Yemen.
  download_url: https://data.humdata.org/dataset/90d299f0-da43-453b-b435-941df85da189/resource/9e7a44ad-18fb-44f4-b600-707a66bbc75e/download/food-security-and-public-health-synthesis-report-yemen-2017.pdf
  format: null
  id: resource_9e7a44ad
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food Security and Public Health Synthesis Report - Yemen - 2017.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_drew_admin1combinedfoodinsecur_20170515
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-05-15'
temporal_resolution: null
title: Yemen - Admin1 - Combined Food Insecurity Phase 2017 and Population Estimates
version: null
vulnerability: null
---
