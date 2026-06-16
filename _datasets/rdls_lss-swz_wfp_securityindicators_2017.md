---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme - mVAM (mobile Vulnerability Analysis and Mapping)
    url: https://data.humdata.org/dataset/wfp-food-security-indicators-for-eswatini
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-food-security-indicators-for-eswatini
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-food-security-indicators-for-eswatini
dataset_id: rdls_lss-swz_wfp_securityindicators_2017
description: 'The World Food Programme (WFP) launched the mobile Vulnerability Analysis
  and Mapping (mVAM) project in 2013, beginning in DRC and Somalia. mVAM uses mobile
  technology to track food security trends in real-time, providing high-frequency
  data that supports humanitarian decision-making. Data collection methods are tailored
  to the needs of each country that mVAM operates in. This dataset contains data from
  the mVAM databank covering various indicators (one per resource).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp-food-security-indicators-for-eswatini]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: WFP mVAM project collects food security data through mobile surveys
    in Eswatini, capturing household-level vulnerability indicators related to food
    insecurity. Survey responses are aggregated into food security statistics and
    indicators that characterize the affected population and food security status
    across the country.
  sources:
  - id: source_1
    license: null
    name: World Food Programme - mVAM (mobile Vulnerability Analysis and Mapping)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp-food-security-indicators-for-eswatini
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity indicators and affected population from mVAM mobile
      survey data
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
          quantity_kind: area
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Eswatini - Food Security Indicators (pblStatsSum: Eswatini - Food
    Security Indicators)'
  download_url: https://data.humdata.org/dataset/e46df1c2-4513-44ac-aa82-a1ba1af50e5e/resource/33b7aca0-750b-4242-886f-c18f1f78bb4a/download/pblstatssum.csv
  format: null
  id: resource_33b7aca0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pblstatssum.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-swz_wfp_securityindicators_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: Eswatini - Food Security Indicators
version: null
vulnerability: null
---
