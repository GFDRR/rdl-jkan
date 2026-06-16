---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/afghanistan-wash-dry-spell-assessment-june-2018
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/afghanistan-wash-dry-spell-assessment-june-2018
dataset_id: rdls_hl-afg_reach_washdryspellassessmentjun_201806
description: 'The overall objective of the assessment is to inform the response of
  the Water, Sanitation and Hygiene (WASH) Cluster for the ongoing dry spell in Afghanistan.
  The assessment aims at supporting the Cluster to better identify target population
  groups, priority areas and relevant interventions.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-wash-dry-spell-assessment-june-2018]'
details: 'REACH would like to acknowledge the contribution of the following partners
  that supported the planning and data collection of this assessment: Global WASH
  Cluster, Afghanistan WASH Cluster, and ACTED. Raw data set and cleaning log are
  available upon request.'
exposure: []
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
      process: hydrological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The assessment collected qualitative and quantitative data through
    key informant interviews conducted at Community Development Councils and informal
    settlements across Afghanistan to document the impacts of the June 2018 dry spell
    on water, sanitation, and hygiene conditions and identify affected population
    groups and priority areas for humanitarian response.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-wash-dry-spell-assessment-june-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by dry spell conditions impacting water availability
      and sanitation access
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
  description: Afghanistan WASH Dry Spell Assessment June 2018 (Excel)
  download_url: https://data.humdata.org/dataset/0734d88c-7833-401e-90d6-1cc78e007823/resource/6a316a3d-7a72-4cb6-9ef7-e0067c0906a1/download/reach_afg_dataset_wash_dry_spell_assessment_june2018.xlsx
  format: null
  id: resource_6a316a3d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_AFG_Dataset_WASH_Dry_Spell_Assessment_June2018.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_reach_washdryspellassessmentjun_201806
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
  end: '2018-06-21'
  start: '2018-06-04'
temporal_resolution: null
title: Afghanistan WASH Dry Spell Assessment June 2018
version: null
vulnerability: null
---
