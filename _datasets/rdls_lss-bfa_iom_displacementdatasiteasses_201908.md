---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/burkina-faso-displacement-data-site-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burkina-faso-displacement-data-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burkina-faso-displacement-data-site-assessment-iom-dtm
dataset_id: rdls_lss-bfa_iom_displacementdatasiteasses_201908
description: 'The dataset contains IDPS and returnees data from Eastern region of
  Burkina Faso at sub-national level. The dataset also contains needs of displaced
  population.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-faso-displacement-data-site-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted site assessments in Eastern Burkina Faso following
    standardized displacement tracking methodology to enumerate internally displaced
    persons and returnees, document their locations and characteristics, and assess
    humanitarian needs at displacement sites. The dataset aggregates sub-national
    level displacement and needs data from Round 1 assessments.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-faso-displacement-data-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees from conflict/insecurity
      in Eastern Burkina Faso
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Humanitarian needs assessment of displaced population at displacement
      sites
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the data collected during the first round of
    collection, which took place in 34 localities in the Eastern region between August
    6 and 18, 2019. In the first round, the DTM identified 10,293 displaced persons
    (1 531 households).
  download_url: https://data.humdata.org/dataset/7df7ab69-9ab5-4043-a927-78aecc97774b/resource/cb10bb18-bef3-4040-ac01-4008a2677100/download/dtm-burkina-faso-site-assessment-round-1.xlsx
  format: null
  id: resource_cb10bb18
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burkina Faso Site Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_iom_displacementdatasiteasses_201908
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-08-18'
  start: '2019-08-06'
temporal_resolution: null
title: Burkina Faso Displacement Data - Site Assessment [IOM DTM]
version: null
vulnerability: null
---
