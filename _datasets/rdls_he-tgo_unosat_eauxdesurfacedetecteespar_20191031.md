---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-images-satellite-a-lacs-et-alentours-togo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-images-satellite-a-lacs-et-alentours-togo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-images-satellite-a-lacs-et-alentours-togo
dataset_id: rdls_he-tgo_unosat_eauxdesurfacedetecteespar_20191031
description: "UNOSAT code: FL20191029TGO Cette carte illustre l'\xE9tendue des eaux\
  \ de surface d\xE9tect\xE9es par images satellite (Sentinel-1, image du 26 Octobre\
  \ 2019) \xE0 dans la pr\xE9fecture de Lacs et alentours, R\xE9gion Maritime, Togo.\
  \ Dans la zone analys\xE9e d'environs 250,000 ha, environ 8,000 personnes sont potentiellement\
  \ expos\xE9es aux 4060 ha d'eaux de surface d\xE9tect\xE9es le 26 Octobre 2019.\
  \ Ceci est une image pr\xE9liminaite qui n'a pas \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Merci d'envoyer vos commentaires \xE0 UNITAR-UNOSAT.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-images-satellite-a-lacs-et-alentours-togo]"
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
    description: Approximately 8,000 people potentially exposed to detected surface
      water in the study area
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery
    from 26 October 2019 using change detection analysis to identify surface water
    extent in Lacs prefecture. The satellite-derived water surface polygons (4,060
    ha detected) were vectorized and attributed with sensor metadata, acquisition
    date, and area measurements to produce preliminary flood extent mapping without
    field validation.
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
- href: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-images-satellite-a-lacs-et-alentours-togo
  rel: source
loss: null
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
  description: "Eaux de surface d\xE9tect\xE9es par images satellite \xE0 Lacs et\
    \ alentours, Togo (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TG/FL20191029TGO/FL20191029TGO_gdb.zip
  format: Geodatabase
  id: resource_826aebd1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191029TGO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par images satellite \xE0 Lacs et\
    \ alentours, Togo (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/TG/FL20191029TGO/FL20191029TGO_SHP.zip
  format: null
  id: resource_7713688b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191029TGO_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tgo_unosat_eauxdesurfacedetecteespar_20191031
spatial:
  bbox: null
  centroid: null
  countries:
  - TGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-31'
temporal_resolution: null
title: "Eaux de surface d\xE9tect\xE9es par images satellite \xE0 Lacs et alentours,\
  \ Togo"
version: null
vulnerability: null
---
