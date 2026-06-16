---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unhcr-bgd-shelter-2019-v2-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-shelter-2019-v2-1
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-bgd-shelter-2019-v2-1
dataset_id: rdls_el-bgd_unhcr_shelterneedassessmentcoxs_2019
description: 'Ensuring adequate and safe shelter for the refugees has been the core
  part of UNHCR''s response in the Rohingya Refugee Crisis Operation from the beginning
  of influx. Moving forward from emergency shelter kits (ESK) distribution to upgrade
  shelter kits (USK) distribution, in 2019 UNHCR has initiated a need based targeted
  shelter repair and replacement assistance to maintain adequate shelter conditions.
  In line with this approach, condition of the shelters have been assessed in order
  to identify the individual shelter needs and specific needs of vulnerable families
  by the technical staff of shelter partners according to criteria and information
  have been collected through GIS tool. A total of 59,920 shelters were assessed.
  Based on the outcome of the assessment, most vulnerable shelters have been provided
  shelter support for Repair and Replacement and less vulnerable shelters are also
  receiving support for repair and replacement.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/unhcr-bgd-shelter-2019-v2-1]'
details: The data must be requested via the resource download link
exposure:
- asset_type:
    description: Shelter structures in Cox's Bazar refugee camps assessed for condition
      and repair needs
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNHCR technical staff conducted a complete enumeration shelter condition
    assessment in Cox's Bazar refugee camps in 2019 to identify shelter damage and
    repair/replacement needs. The assessment targeted individual shelters to classify
    vulnerability and prioritize assistance for shelter upgrade and repair interventions.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-bgd-shelter-2019-v2-1
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Shelter damage and need for repair/replacement assessed in Cox's
      Bazar camps
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
        metric: loss
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
- access_url: https://microdata.unhcr.org/index.php/auth/login/?destination=catalog/209/get-microdata
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Clicking 'Download' leads outside HDX where you can request access
    to the data in csv, xlsx & dta formats
  download_url: null
  format: null
  id: resource_b13f8251
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bangladesh - Shelter Need Assessment Cox's Bazar 2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Shelter Need Assessment Cox's Bazar 2019 (Contains information
    about the dataset's metadata and data)
  download_url: https://microdata.unhcr.org/index.php/catalog/209/pdf-documentation
  format: null
  id: resource_36c39c2f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Codebook
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_unhcr_shelterneedassessmentcoxs_2019
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
  end: '2019-09-30'
  start: '2019-07-05'
temporal_resolution: null
title: Bangladesh - Shelter Need Assessment Cox's Bazar 2019
version: null
vulnerability: null
---
