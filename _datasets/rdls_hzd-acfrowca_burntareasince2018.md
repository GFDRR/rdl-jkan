---
attributions:
- entity:
    affiliation: null
    email: null
    name: COPERNICUS Land Monitoring Service Burnt Area (BA) product v4
    url: https://data.humdata.org/dataset/west-and-central-africa-burnt-area
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Administrative Boundaries
    url: https://data.humdata.org/dataset/west-and-central-africa-burnt-area
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/west-and-central-africa-burnt-area
creator:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/west-and-central-africa-burnt-area
dataset_id: rdls_hzd-acfrowca_burntareasince2018
description: "Monthly and annual burnt area statistics (in sqkm) are calculated from\
  \ 2018 onwards at Admin 0, 1, and 2 levels. The source data is the Burnt Area (BA)\
  \ product from COPERNICUS Land Monitoring Service v4 (300m resolution), reprocessed\
  \ to extract bushfire occurrence statistics. Administrative boundaries are provided\
  \ by OCHA https://data.humdata.org/dataset/west-and-central-africa-administrative-boundaries-levels\
  \ GeoTIFF raster files and shapefile vector files are available for download at\
  \ https://geosahel.info For more information, please visit: www.sigsahel.info Des\
  \ statistiques mensuelles et annuelles de surfaces br\xFBl\xE9es (en km\xB2) sont\
  \ calcul\xE9es \xE0 partir de 2018 aux niveaux administratif 0, 1 et 2. La source\
  \ des donn\xE9es est le produit \xAB Burnt Area (BA) \xBB du service de surveillance\
  \ des terres COPERNICUS v4 (r\xE9solution de 300 m), retrait\xE9 pour extraire des\
  \ statistiques sur les feux de brousse. Les limites administratives sont fournies\
  \ par OCHA : https://data.humdata.org/dataset/west-and-central-africa-administrative-boundaries-levels\
  \ Les fichiers raster GeoTIFF et les fichiers vectoriels shapefile sont disponibles\
  \ au t\xE9l\xE9chargement sur https://geosahel.info Pour plus d'informations, veuillez\
  \ consulter : www.sigsahel.info. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/west-and-central-africa-burnt-area]"
details: null
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
      intensity_measure: AA:km2
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Monthly and annual burnt area statistics were calculated from COPERNICUS
    Land Monitoring Service Burnt Area product v4 (300m resolution) through reprocessing
    of remote sensing data. Burnt area values were aggregated at administrative levels
    (Admin 0, 1, and 2) using OCHA administrative boundaries to produce tabular statistics
    in spreadsheet format covering West and Central Africa from 2018 onwards.
  sources:
  - id: source_1
    license: null
    name: COPERNICUS Land Monitoring Service Burnt Area (BA) product v4
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: OCHA Administrative Boundaries
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/west-and-central-africa-burnt-area
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
  description: West and Central Africa - Burnt Area since 2018 (Excel)
  download_url: https://geosahel.info/MetaDownload/FireMonitor/BURNT-AREA_ADM0.xlsx
  format: null
  id: resource_0ae1bf20
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BURNT-AREA_ADM0.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West and Central Africa - Burnt Area since 2018 (Excel)
  download_url: https://geosahel.info/MetaDownload/FireMonitor/BURNT-AREA_ADM1.xlsx
  format: null
  id: resource_37525680
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BURNT-AREA_ADM1.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West and Central Africa - Burnt Area since 2018 (Excel)
  download_url: https://geosahel.info/MetaDownload/FireMonitor/BURNT-AREA_ADM2.xlsx
  format: null
  id: resource_d4a558f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BURNT-AREA_ADM2.xlsx
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-acfrowca_burntareasince2018
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  - BFA
  - CAF
  - TCD
  - CIV
  - GMB
  - GHA
  - GIN
  - GNB
  - KEN
  - LBR
  - MLI
  - MRT
  - NER
  - NGA
  - SEN
  - SLE
  - TGO
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: West and Central Africa - Burnt Area since 2018
version: null
vulnerability: null
---
