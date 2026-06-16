---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM Index for Risk Management
    url: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Cambodia Ministry of Environment
    url: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
dataset_id: rdls_el-khm_inform_childrensclimateriskindex_20250114
description: 'Developed by the Cambodia Ministry of Environment in collaboration with
  UNICEF, the Children''s Climate Risk Index for Cambodia (CCRI) offers an in-depth
  look at how children in Cambodia are exposed to and affected by climate and environmental
  hazards. This index is the first of its kind, focusing on the lowest administrative
  level (commune), that provides a detailed view of children''s vulnerabilities based
  on their access to essential services such as health, education, WASH (Water, Sanitation,
  and Hygiene), and social and child protection. It has been adapted from the framework
  of UNICEF''s global Children''s Climate Risk Index. The CCRI-Cambodia is developed
  as a subnational adaptation of UNICEF''s global Children''s Climate Risk Index.
  It also draws heavily from the methodology and approach of the Index for Risk Management
  (INFORM) as a primary reference. It incorporates Cambodia-specific components and
  indicators from the two pillars used in the global CCRI. Pillar 1 estimates children''s
  exposure to multiple climate and environmental hazards, shocks and disasters, while
  pillar 2 assesses children''s vulnerability to such threats. The CCRI adopts a multi-shock
  and multi-sectoral approach and, importantly, goes beyond a sole focus on climate
  risks to encompass broader and overlapping natural and environmental shocks that
  affect children at the lowest of Cambodia''s four-tier administrative system (national,
  provincial, district and commune). It also considers critical factors of vulnerability
  across social sectors: child health and nutrition, water, sanitation and hygiene
  (WASH), child protection, education and livelihoods and social protection. It is
  therefore a significant milestone towards identifying where children (under 18 years)
  in the country are most at risk of climate and environmental shocks because of a
  lack of access to critical social services. The CCRI-Cambodia model can also be
  found on the GeoSight dashboard, which is a geospatial platform intended to provide
  an easy-to-use and open-source cartographic visualization of the CCRI Cambodia model
  created by UNICEF. Link: https://geosight.unicef.org/project/cambodia-ccri-drm-index.
  The Model could also be found on the Cambodia Ministry of Environment. The link:
  https://ncsd.moe.gov.kh/dcc/data-portal/cambodias-childrens-climate-risk-index-ccri.
  An analytical report is also available. The link: https://www.unicef.org/cambodia/reports/childrens-climate-risk-index-cambodia
  The CCRI-Cambodia can further stimulate and facilitate stakeholder engagement at
  the local level and improve collaboration, coordination and collective efforts..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment]'
details: null
exposure:
- asset_type:
    description: Children under 18 years exposed to climate and environmental hazards
      at commune level
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
  description: The Cambodia CCRI integrates probabilistic climate and environmental
    hazard models (drought, extreme heat, riverine floods, high wind) with subnational
    population exposure data and vulnerability indicators across five dimensions (health/nutrition,
    WASH, education, livelihoods/social protection, child protection) to produce a
    composite risk index at commune level. The methodology follows the INFORM risk
    management framework and UNICEF's global CCRI approach, combining simulated hazard
    exposure with service access indicators to assess overall climate and disaster
    risk to children under 18.
  sources:
  - id: source_1
    license: null
    name: UNICEF
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: INFORM Index for Risk Management
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Cambodia Ministry of Environment
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cambodia-children-s-climate-risk-index-ccri-subnational-risk-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Children under 18 affected by drought exposure through impacts on
      livelihoods and food security
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
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Children under 18 affected by extreme heat through health and nutrition
      impacts
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
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Children under 18 affected by riverine flooding through disruption
      to WASH, education, and health services
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
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Children under 18 affected by high wind speed through infrastructure
      disruption and livelihood impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: Cambodia Children's Climate Risk Index (CCRI) subnational risk assessment.
    (UNICEF, global and in country.)
  download_url: https://data.humdata.org/dataset/3a4318e7-ce69-4e55-b377-f1701bc49c2f/resource/5f37c751-536f-48c4-a21e-3c3176708209/download/ccri-cambodia-model.xlsx
  format: null
  id: resource_5f37c751
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CCRI-Cambodia-Model.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cambodia Children's Climate Risk Index (CCRI) subnational risk assessment.
    (PDF)
  download_url: https://data.humdata.org/dataset/3a4318e7-ce69-4e55-b377-f1701bc49c2f/resource/5c38ccf8-6bba-4b04-9696-b234768264aa/download/report-ccri-cambodia.pdf
  format: null
  id: resource_5c38ccf8
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CCRI-Cambodia-Report.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cambodia Children's Climate Risk Index (CCRI) subnational risk assessment.
    (CCRI-Cambodia-Theoretical Framework.pdf)
  download_url: https://data.humdata.org/dataset/3a4318e7-ce69-4e55-b377-f1701bc49c2f/resource/e69e64cc-90ae-411b-ac10-6c98b3794b59/download/ccri-cambodia-theoretical-framework.pdf
  format: null
  id: resource_e69e64cc
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CCRI-Cambodia-Theoretical Framework.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-khm_inform_childrensclimateriskindex_20250114
spatial:
  bbox: null
  centroid: null
  countries:
  - KHM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-01-14'
temporal_resolution: null
title: Cambodia Children's Climate Risk Index (CCRI) subnational risk assessment.
version: null
vulnerability: null
---
