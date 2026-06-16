---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-september-16-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-september-16-2015
dataset_id: rdls_hl-mmr_unosat_geodatalandslideinducedda_20150916
description: 'This map illustrates satellite-detected waters over Tonzang township,
  Chin Division, Myanmar. UNITAR-UNOSAT analyzed imagery collected by the Pleiades
  satellite on 16 September 2015 and detected the presence of a landslide over a mountainous
  area in Tonzang township. As a consequence of the landslide waters have accumulated
  in the area forming a dam. Imagery shows that a total of 34 hectares are covered
  by water. The heavy cloud cover in the area prevents UNOSAT from determining the
  exact dimension of the landslide. This is a preliminary analysis & has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-september-16-2015]'
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
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery collected on 16
    September 2015 over Tonzang Township, Chin Division, Myanmar, comparing multi-temporal
    images to detect a landslide event and the resulting water accumulation forming
    a natural dam. The analysis identified 34 hectares of water coverage but was limited
    by heavy cloud cover preventing precise landslide dimension determination. This
    is a preliminary post-event observation requiring field validation.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-landslide-induced-dam-over-tonzang-township-chin-division-myanmar-september-16-2015
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Water accumulation area (34 hectares) resulting from landslide-induced
      dam formation
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
  id: resource_4160b62d
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
  id: resource_26174ad7
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
slug: rdls_hl-mmr_unosat_geodatalandslideinducedda_20150916
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
  start: '2015-09-16'
temporal_resolution: null
title: Geodata of Landslide induced dam over Tonzang Township, Chin Division, Myanmar
version: null
vulnerability: null
---
