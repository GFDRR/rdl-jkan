---
attributions:
- entity:
    affiliation: null
    email: null
    name: Integrated Phase Classification (IPC)
    url: https://data.humdata.org/dataset/ica-sudan-2018-recurrence-of-food-insecurity-2010-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-recurrence-of-food-insecurity-2010-2017
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-recurrence-of-food-insecurity-2010-2017
dataset_id: rdls_lss-sdn_ochasdn_ica2018recurrencefoodinse_20181122
description: 'This layer contains information about the food security trend analysis
  - by second-level administrative unit - used for the purposes of the Integrated
  Context Analysis (ICA) run in Sudan in 2018. Data source: Integrated Phase Classification
  (IPC), 2010-2017. The main indicator used for the analysis was the recurrence of
  IPC Phases 3 or above out of the number of available rounds.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ica-sudan-2018-recurrence-of-food-insecurity-2010-2017]'
details: https://geonode.wfp.org/layers/geonode%3Asdn_ica_firecurrence_geonode_20180201
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC food security assessments from 2010-2017 were aggregated by second-level
    administrative unit to calculate the recurrence frequency of IPC Phases 3 or above
    (Crisis and Emergency levels) as a trend indicator of food insecurity vulnerability
    for the 2018 Integrated Context Analysis in Sudan.
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
- href: https://data.humdata.org/dataset/ica-sudan-2018-recurrence-of-food-insecurity-2010-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classification (IPC Phases 3+) as a proxy impact
      indicator for drought-affected populations
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
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_firecurrence_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'This layer contains information about the food security trend analysis
    - by second-level administrative unit - used for the purposes of the Integrated
    Context Analysis (ICA) run in Sudan in 2018. Data source: Integrated Phase Classification
    (IPC), 2010-2017. The main indicator used for the analysis was the recurrence
    of IPC Phases 3 or above out of the number of available rounds.'
  download_url: null
  format: null
  id: resource_124ebcf2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Recurrence of Food Insecurity, 2010-2017
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_ica2018recurrencefoodinse_20181122
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
title: ICA Sudan, 2018 - Recurrence of Food Insecurity, 2010-2017
version: null
vulnerability: null
---
