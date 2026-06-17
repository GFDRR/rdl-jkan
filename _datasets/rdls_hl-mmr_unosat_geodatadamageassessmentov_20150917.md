---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015
dataset_id: rdls_hl-mmr_unosat_geodatadamageassessmentov_20150917
description: 'This map illustrates satellite-detected damaged structures over Tuikhingzang
  town, Tonzang township, Chin Division, Myanmar. After a reported landslide induced
  dam that ruptured on 28 August 2015, UNITAR-UNOSAT analyzed imagery collected by
  the Pleiades satellite on 16 September 2015 and identified an area severely affected
  by a mudslide. Wide agricultural areas appear affected and the town of Tuikhingzang
  is partially covered by mud. UNOSAT identified a total of 141 destroyed structures
  and 48 severely damaged structures in the area. Local roads are also affected and
  a bridge has been completely destroyed. In addition two IDP settlements are visible
  1 and 3 km northeast of the town and a total of 260 possible tent shelters were
  identified. This is a preliminary analysis & has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared Pleiades satellite imagery collected
    on 16 September 2015 against pre-event baseline imagery to identify structural
    damage and affected areas resulting from a landslide-induced dam rupture on 28
    August 2015. Visual interpretation of satellite imagery enabled detection and
    mapping of 141 destroyed and 48 severely damaged structures, as well as delineation
    of mudslide extent affecting agricultural land and infrastructure in Tuikhingzang
    town.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-over-tuikhingzang-tonzang-township-chin-division-september-17-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 141 destroyed structures and 48 severely damaged structures from
      mudslide
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Local roads and bridge damage from mudslide event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Wide agricultural areas affected by mudslide inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin
    Division, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_d1a77706
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin
    Division, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_16dda7c3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_geodatadamageassessmentov_20150917
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-09-17'
temporal_resolution: null
title: Geodata of Damage Assessment over Tuikhingzang, Tonzang Township, Chin Division,
  Myanmar
version: null
vulnerability: null
---
