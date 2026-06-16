---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA-VIIRS satellite imagery
    url: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020
dataset_id: rdls_hel-nic_unosat_inundacionesenentreel13y1_20201118
description: "UNOSAT code: TC20201116NIC Este mapa ilustra las inundaciones detectadas\
  \ por el sat\xE9lite NOAA-VIIRS en Nicaragua entre el 13 y 17 de Noviembre. Dentro\
  \ del \xE1rea analizada de aproximadamente 95,000 km2, un total de aproximadamente\
  \ 2,000 km2 de tierras parecen estar inundadas. Basado en los datos de poblaci\xF3\
  n de Worldpop y la extensi\xF3n de las aguas superficiales detectadas, alrededor\
  \ de 100,000 personas est\xE1n potencialmente expuestas o viven cerca de \xE1reas\
  \ inundadas. La poblaci\xF3n potencialmente expuesta se encuentra principalmente\
  \ en el departamento de Chinandega con ~25,000 habitantes, en el departamento de\
  \ Manague con ~16,000 habitantes, y em el departamento de Atl\xE1ntico Norte con\
  \ 10,000 habitantes. Se trata de un an\xE1lisis preliminar que a\xFAn no ha sido\
  \ validado en el terreno. Por favor env\xEDe comentarios a UNITAR-UNOSAT.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020]"
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
    description: Residential population potentially exposed to or living near detected
      inundated areas based on WorldPop data
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared multi-temporal NOAA-VIIRS satellite imagery\
    \ from 13-17 November 2020 to detect surface water extent changes during cyclone-induced\
    \ flooding. Detected inundation areas (~2,000 km\xB2) were intersected with WorldPop\
    \ gridded population data to estimate potentially exposed population (~100,000\
    \ people), primarily in Chinandega department."
  sources:
  - id: source_1
    license: null
    name: NOAA-VIIRS satellite imagery
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
- href: https://data.humdata.org/dataset/inundaciones-en-nicaragua-entre-el-13-y-17-de-noviembre-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooding from November 2020 inundation
      event
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
  description: Inundaciones en Nicaragua entre el 13 y 17 de Noviembre 2020 (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NI/TC20201116NIC/TC20201116NIC_gdb.zip
  format: Geodatabase
  id: resource_73bab74c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201116NIC_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Inundaciones en Nicaragua entre el 13 y 17 de Noviembre 2020 (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/NI/TC20201116NIC/TC20201116NIC_SHP.zip
  format: null
  id: resource_55ab73ef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201116NIC_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nic_unosat_inundacionesenentreel13y1_20201118
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-18'
temporal_resolution: null
title: Inundaciones en Nicaragua entre el 13 y 17 de Noviembre 2020
version: null
vulnerability: null
---
