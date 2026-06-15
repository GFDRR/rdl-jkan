---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-and-cibao-sur-regions-dominican-republic-as-of-18-november-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-and-cibao-sur-regions-dominican-republic-as-of-18-november-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-and-cibao-sur-regions-dominican-republic-as-of-18-november-
dataset_id: rdls_he-dom_unosat_detectedwaterextentcibaon_20231121
description: "UNOSAT code: FL20231120DOM, GDACS ID: 1102342 This map illustrates cumulative\
  \ satellite-detected water extent in CIbao Nordeste and Cibao Sur Regions, Dominican\
  \ Republic as observed from a Sentinel-1 image acquired on the 18 November 2023\
  \ at 18:53 local time. Within the extent of this map, about 55 km\xC2\xB2 of land\
  \ appears to be affected with flood waters and about 10,500 people are potentially\
  \ exposed to flood waters This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to backscattering properties of the radar signal.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-and-cibao-sur-regions-dominican-republic-as-of-18-november-]"
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
    description: Population potentially exposed to satellite-detected flood waters
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 SAR imagery acquired on 18 November 2023 was analyzed by
    UNOSAT through visual interpretation and change detection to identify cumulative
    water extent. Satellite-detected inundation polygons were delineated and intersected
    with population grids to estimate exposure. The dataset represents preliminary
    post-event observations without field validation.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-and-cibao-sur-regions-dominican-republic-as-of-18-november-
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extent in Cibao Nordeste and Cibao Sur Regions,
    Dominican Republic as of 18 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3747/FL20231120DOM_gdb.zip
  format: Geodatabase
  id: resource_137e5792
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Cibao Nordeste and Cibao Sur Regions,
    Dominican Republic as of 18 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3747/FL20231120DOM_SHP.zip
  format: null
  id: resource_550955e0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Cibao Nordeste and Cibao Sur Regions,
    Dominican Republic as of 18 November 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3747/UNOSAT_Population_Exposure_FL20231120DOM_WestDOM_18Nov2023.xlsx
  format: null
  id: resource_bcc1f5be
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20231120DOM_WestDOM_18Nov2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-dom_unosat_detectedwaterextentcibaon_20231121
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-21'
temporal_resolution: null
title: Satellite detected water extent in Cibao Nordeste and Cibao Sur Regions, Dominican
  Republic as of 18 November 2023
version: null
vulnerability: null
---
