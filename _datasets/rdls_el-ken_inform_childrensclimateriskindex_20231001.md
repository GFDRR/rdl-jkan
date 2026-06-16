---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM Index for Risk Management
    url: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment
dataset_id: rdls_el-ken_inform_childrensclimateriskindex_20231001
description: 'This is a Children''s Climate and Disaster Risk model (CCRI-DRM) Kenya
  model created by UNICEF. The Kenyan CCRI-DRM subnational risk assessment initiative
  is a joint effort between UNICEF, Kenya national authorities and stakeholders, and
  international partners to enrich, create and use child-inclusive climate and disaster
  risk data. The initiative aims to improve the understanding and management of risks
  that children, young people, families and their communities face from natural hazards,
  climate and environmental hazards, shocks and stresses, and disasters. The approach
  and processes for subnational adaptations of the Index for Risk Management (INFORM)
  model provide the main reference for the development of the subnational CCRI-DRM.
  This analysis is composed of two main pillars that are indexed and combined into
  a final risk score: - Pillar 1: Exposure to Shocks & Stressors - Pillar 2: Child
  Vulnerability Reference layers have been added as incomplete but vital datasets
  that can improve contextual understanding of the lives of children where data is
  available. Please note that the number values of the shock exposure indicators included
  in the first pillar of the model are ESTIMATES of children under 18 exposed to the
  different types of shocks and stresses. These estimates are data derived from a
  combination of hazard and population layers and should not be treated as official
  or specific numbers. The Kenya CCRI-DRM model can also be found on the GeoSight
  dashboard, which is a geospatial platform intended to provide an easy-to-use and
  open-source cartographic visualization of the CCRI-DRM Kenya model created by UNICEF.
  (Link: https://geosight.unicef.org/project/kenya-ccri-drm-dashboard). The Model
  could also be found on the Kenya Ministry Of Environment, Climate Change & Forestry.
  The link: https://environment.go.ke/ccri-drm-portal/.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment]'
details: null
exposure:
- asset_type:
    description: Children under 18 years exposed to multiple hazards including drought,
      heat, floods, and disease vectors
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
  description: The CCRI-DRM Kenya model integrates hazard exposure data (drought via
    VCI, temperature extremes, riverine floods at 50-year return period) with child
    population counts and vulnerability indicators (health, nutrition, WASH, livelihoods)
    across 47 Kenyan counties. The methodology follows the INFORM risk management
    approach and global UNICEF CCRI framework, combining gridded hazard datasets with
    subnational administrative data to produce a composite risk index ranking counties
    by child climate and disaster risk.
  sources:
  - id: source_1
    license: null
    name: UNICEF
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: INFORM Index for Risk Management
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-children-s-climate-risk-index-disaster-risk-model-ccri-drm-subnational-risk-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Children exposed to water scarcity and at least moderate drought
      conditions
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Children exposed to high heatwave frequency and extreme high temperatures
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
  - asset_category: population
    asset_dimension: population
    description: Children exposed to 50-year return period riverine floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  description: Kenya Children's Climate Risk Index-Disaster Risk Model (CCRI-DRM)
    subnational risk assessment. A composite index that includes risk data on child
    exposure and vulnerability to hazards, shocks and stresses. (Excel)
  download_url: https://data.humdata.org/dataset/17582fbe-00b1-4077-b921-4890bfe525e5/resource/a97a88fc-ed90-4756-ac94-135ac34173b7/download/kenya_ccridrm_model_v2.3.xlsx
  format: null
  id: resource_a97a88fc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kenya_CCRIDRM_Model_v2.3.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ken_inform_childrensclimateriskindex_20231001
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-01'
temporal_resolution: null
title: Kenya Children's Climate Risk Index-Disaster Risk Model (CCRI-DRM) subnational
  risk assessment. A composite index that includes risk data on child exposure and
  vulnerability to hazards, shocks and stresses.
version: null
vulnerability: null
---
