---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/south-sudan-displacement-multi-sectoral-village-assessment-idps-returnees-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/south-sudan-displacement-multi-sectoral-village-assessment-idps-returnees-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/south-sudan-displacement-multi-sectoral-village-assessment-idps-returnees-iom-dtm
dataset_id: rdls_lss-ssd_iom_displacementmultisectoral_2016
description: 'The assessment contains IDPs and Returnees data at village level. The
  data is gender and age disaggregated and also has number of vulnerable population
  and the needs assessment.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-displacement-multi-sectoral-village-assessment-idps-returnees-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted village-level assessments across South Sudan from
    May 2016 to November 2019, collecting data on IDP and returnee populations disaggregated
    by gender and age. The assessment integrated multi-sectoral needs evaluation to
    identify vulnerable populations, producing a structured dataset of displacement
    impacts at the village administrative level.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) - Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-displacement-multi-sectoral-village-assessment-idps-returnees-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees from conflict-related
      displacement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Vulnerable population identified through multi-sectoral needs assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The dataset contains IDPs and returnees data at village level starting
    from May 16 upto Nov 19
  download_url: https://data.humdata.org/dataset/27a2c58e-eccc-4d7c-8782-7b7fd2272240/resource/47a04948-0f01-4ebc-b873-dc20c7906bd7/download/dtm-south-sudan-village-assessment-may-16-to-nov-19.xlsx
  format: null
  id: resource_47a04948
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM South Sudan Village Assessment May-16 to Nov-19
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_iom_displacementmultisectoral_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-11-22'
  start: '2016-05-01'
temporal_resolution: null
title: South Sudan Displacement - Multi-Sectoral Village Assessment -IDPs - Returnees
version: null
vulnerability: null
---
