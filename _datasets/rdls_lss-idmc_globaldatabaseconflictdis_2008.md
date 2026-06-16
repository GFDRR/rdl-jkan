---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/gidd_conflict_disasters_context_sadd
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/gidd_conflict_disasters_context_sadd
dataset_id: rdls_lss-idmc_globaldatabaseconflictdis_2008
description: 'The Global Internal Displacement Database (GIDD) presents a global dataset
  compiling the main metrics reported by IDMC from 2008 to 2023. Internally displaced
  persons are defined according to the 1998 Guiding Principles (http://www.internal-displacement.org/publications/1998/ocha-guiding-principles-on-internal-displacement)
  as people or groups of people who have been forced or obliged to flee or to leave
  their homes or places of habitual residence, in particular as a result of armed
  conflict, or to avoid the effects of armed conflict, situations of generalized violence,
  violations of human rights, or natural or human-made disasters and who have not
  crossed an international border. ''People Displaced'' refers to the number of people
  living in displacement as of the end of each year. ''New Displacement'' refers to
  the number of new cases or incidents of displacement recorded, rather than the number
  of people displaced. This is done because people may have been displaced more than
  once. Contains data from IDMC''s Global Internal Displacement Database.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gidd_conflict_disasters_context_sadd]'
details: For more information on the methodology visit https://www.internal-displacement.org/monitoring-tools/.
  For any question or API request contact us at ch.datainfo@idmc.ch.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IDMC aggregates reported internal displacement metrics from multiple
    national and international sources covering conflict and disaster-induced displacement
    from 2008 to 2023. Data is curated, validated, and compiled into a global database
    with demographic disaggregation to provide comprehensive loss impact records across
    multiple hazard types.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gidd_conflict_disasters_context_sadd
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement caused by flood disasters
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
    description: Internal displacement caused by earthquake disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
    description: Internal displacement caused by strong wind disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
    description: Internal displacement caused by drought disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
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
    description: Internal displacement caused by wildfire disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_5
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
  description: The GIDD data includes SADD data based on population projections for
    the time period of 2008 to 2023
  download_url: https://helix-tools-api.idmcdb.org/external-api/gidd/displacements/displacement-export/?release_environment=RELEASE&start_year=2008&end_year=2023&client_id=IDMCWSHSOLO009&release_environment=RELEASE
  format: null
  id: resource_39a06100
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDMC_Internal_Displacement_Conflict-Violence_Disasters
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idmc_globaldatabaseconflictdis_2008
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2008-01-01'
temporal_resolution: null
title: 'Global Internal Displacement Database: Conflict - Disasters'
version: null
vulnerability: null
---
