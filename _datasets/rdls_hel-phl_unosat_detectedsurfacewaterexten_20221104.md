---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil
dataset_id: rdls_hel-phl_unosat_detectedsurfacewaterexten_20221104
description: 'UNOSAT code TC20221028PHL, GDACS Id: 1000942 This map illustrates the
  extent of surface waters in Bulacan, Nueva Ecija, Pampanga, and Tarlac Provinces,
  Region III, Philippines as observed from a TerraSAR-X image acquired on 3 November
  2022 at 05:59 local time. Within the analysis extent of about 1,800 km2, approximately
  160 km2 of land appears to be inundated and 140 km2 of croplands appear to be likely
  affected by the flood waters. Based on Worldpop population data and detected surface
  waters, approximately 84,000 people are potentially exposed or living close to flooded
  areas. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT). Important
  note: Flood analysis from radar images may underestimate the presence of standing
  waters in built-up areas and densely vegetated areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
- asset_type:
    description: Cropland area affected by flood waters
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: TerraSAR-X satellite imagery acquired on 3 November 2022 was analyzed
    by UNOSAT to detect surface water extents through multi-temporal image comparison.
    Detected inundation areas were intersected with WorldPop population grids to estimate
    population exposure, and cropland areas were identified as affected by flood waters.
    The resulting geodatabase and shapefile products contain observed flood extent
    polygons with area calculations across four provinces in Region III, Philippines.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/surface-water-extents-in-bulacan-nueva-ecija-pampanga-and-tarlac-provinces-region-iii-phil
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural loss from flood inundation affecting croplands
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood exposure in inundated areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected surface water extents in Bulacan, Nueva Ecija, Pampanga,
    and Tarlac Provinces, Region III, Philippines as of 3 November 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3438/TC20221028PHL_gdb.zip
  format: Geodatabase
  id: resource_39b1a242
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221028PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected surface water extents in Bulacan, Nueva Ecija, Pampanga,
    and Tarlac Provinces, Region III, Philippines as of 3 November 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3438/TC20221028PHL_SHP.zip
  format: null
  id: resource_eb1ee7fb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221028PHL_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected surface water extents in Bulacan, Nueva Ecija, Pampanga,
    and Tarlac Provinces, Region III, Philippines as of 3 November 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3438/UNOSAT_Population_Exposure_TC20221028PHL_BulacanNuevaEcijaPampangaTarlac_03Nov2022.csv
  format: null
  id: resource_c8861f8a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20221028PHL_BulacanNuevaEcijaPampangaTarlac_03Nov2022.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_detectedsurfacewaterexten_20221104
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-04'
temporal_resolution: null
title: Satellite detected surface water extents in Bulacan, Nueva Ecija, Pampanga,
  and Tarlac Provinces, Region III, Philippines as of 3 November 2022
version: null
vulnerability: null
---
