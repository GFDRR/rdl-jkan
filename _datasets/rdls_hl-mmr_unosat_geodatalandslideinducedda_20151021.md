---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-october-21-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-october-21-2015
dataset_id: rdls_hl-mmr_unosat_geodatalandslideinducedda_20151021
description: 'This map illustrates satellite-detected waters over Tonzang township,
  Chin Division, Myanmar. UNITAR-UNOSAT analyzed imagery collected by the WorldView-2
  satellite on 17 October 2015 to assess the status of a landslide induced dam in
  Tonzang township. Imagery shows that there has been an increase in the satellite
  detected waters in the area and a total of 54 hectares are covered by water as of
  17 October 2015. This means an increase of 59% since last UNOSAT analysis with imagery
  from 16 September 2015 when 34 hectares of land were covered by water. The increase
  on the satellite detected waters might have been slightly overestimated as extensive
  cloud cover in the area as of 16 September prevented UNOSAT from analyzing certain
  areas of the landslide. This is a preliminary analysis & has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-october-21-2015]'
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
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared WorldView-2 satellite imagery acquired on
    17 October 2015 with prior imagery from 16 September 2015 to detect changes in
    water extent caused by a landslide-induced dam in Tonzang Township. Water bodies
    were manually delineated and quantified by area (hectares), with confidence assessments
    and field validation flags recorded in the geodatabase.
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
- href: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-october-21-2015
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Water impoundment area created by landslide-induced dam, measured
      at 54 hectares as of 17 October 2015
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_1
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
  description: Geodata of Landslide induced dam over Tonzang Township, Chin Division,
    Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_5e74f907
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
  description: Geodata of Landslide induced dam over Tonzang Township, Chin Division,
    Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_f68e54ae
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
slug: rdls_hl-mmr_unosat_geodatalandslideinducedda_20151021
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
  start: '2015-10-21'
temporal_resolution: null
title: Geodata of Landslide induced dam over Tonzang Township, Chin Division, Myanmar
version: null
vulnerability: null
---
