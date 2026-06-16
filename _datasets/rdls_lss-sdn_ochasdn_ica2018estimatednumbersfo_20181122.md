---
attributions:
- entity:
    affiliation: null
    email: null
    name: Integrated Phase Classification (IPC)
    url: https://data.humdata.org/dataset/ica-sudan-2018-estimated-numbers-of-food-insecure-people-2014-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-estimated-numbers-of-food-insecure-people-2014-2017
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-estimated-numbers-of-food-insecure-people-2014-2017
dataset_id: rdls_lss-sdn_ochasdn_ica2018estimatednumbersfo_20181122
description: 'This layer contains information about the numbers of food insecure people
  - by first-level administrative unit - estimated for the purposes of the Integrated
  Context Analysis (ICA) run in Mali in 2017. It should be noted that estimates of
  food insecure people were available only starting from 2014 onwards and, due to
  access constraints, some of the states were not covered by the survey. Data source:
  Integrated Phase Classification (IPC), 2014-2017. The main indicators used for the
  analysis were the percentage of food insecure population for long-term planning
  and the additional population figures in case of a major shock.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ica-sudan-2018-estimated-numbers-of-food-insecure-people-2014-2017]'
details: https://geonode.wfp.org/layers/geonode%3Asdn_ica_adm1_estimatedfipeople_geonode_20180201
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Food insecurity population estimates were sourced from IPC phase classifications\
    \ (2014\u20132017) and aggregated to first-level administrative units in Sudan.\
    \ The Integrated Context Analysis (ICA) framework applied by WFP used these figures\u2014\
    including long-term planning population percentages and additional food insecure\
    \ population counts\u2014to characterize chronic and acute food insecurity conditions,\
    \ with some states excluded due to access constraints."
  sources:
  - id: source_1
    license: null
    name: Integrated Phase Classification (IPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ica-sudan-2018-estimated-numbers-of-food-insecure-people-2014-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated numbers of food insecure people by first-level administrative
      unit in Sudan, derived from IPC classifications for 2014-2017, including long-term
      planning population and additional food insecure population figures
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_adm1_estimatedfipeople_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'This layer contains information about the numbers of food insecure
    people - by first-level administrative unit - estimated for the purposes of the
    Integrated Context Analysis (ICA) run in Mali in 2017. It should be noted that
    estimates of food insecure people were available only starting from 2014 onwards
    and, due to access constraints, some of the states were not covered by the survey.
    Data source: Integrated Phase Classification (IPC), 2014-2017. The main indicators
    used for the analysis were the percentage of food insecure population for long-term
    planning and the additional population figures in case of a major shock.'
  download_url: null
  format: null
  id: resource_6b1148b8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Estimated Numbers of Food Insecure People, 2014-2017
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_ica2018estimatednumbersfo_20181122
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-22'
temporal_resolution: null
title: ICA Sudan, 2018 - Estimated Numbers of Food Insecure People, 2014-2017
version: null
vulnerability: null
---
