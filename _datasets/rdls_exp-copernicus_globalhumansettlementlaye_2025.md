---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/global-human-settlement-layer-ghsl
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/global-human-settlement-layer-ghsl
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/global-human-settlement-layer-ghsl
dataset_id: rdls_exp-copernicus_globalhumansettlementlaye_2025
description: 'Open and free data for assessing the human presence on the planet. The
  Global Human Settlement Layer (GHSL) project produces global spatial information,
  evidence-based analytics, and knowledge describing the human presence on the planet.
  The GHSL relies on the design and implementation of spatial data processing technologies
  that allow automatic data analytics and information extraction from large amounts
  of heterogeneous geospatial data including global, fine-scale satellite image data
  streams, census data, and crowd sourced or volunteered geographic information sources.
  The JRC, together with the Directorate-General for Regional and Urban Policy (DG
  REGIO) and Directorate-General for Defence Industry and Space (DG DEFIS) are working
  towards a regular and operational monitoring of global built-up and population based
  on the processing of Sentinel Earth Observation data produced by European Copernicus
  space program. In addition, the EU Agency for the Space Programme (EUSPA) undertakes
  activities related to user uptake of data, information and services.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/global-human-settlement-layer-ghsl]'
details: 'Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface
  grid, derived from Sentinel2 composite and Landsat, multitemporal (1975-2030). European
  Commission, Joint Research Centre (JRC) PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea
  doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA Schiavina M., Freire S., Carioli
  A., MacManus K. (2023): GHS-POP R2023A - GHS population grid multitemporal (1975-2030).
  European Commission, Joint Research Centre (JRC) PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe
  doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE'
exposure:
- asset_type:
    description: Built-up surface area derived from satellite imagery classification
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Gridded population distribution estimated from census data and satellite
      imagery
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Global Human Settlement Layer integrates fine-scale satellite imagery,
    census data, and crowdsourced geographic information through automated spatial
    data processing technologies to produce gridded estimates of built-up surfaces
    and population distribution at global scale.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-human-settlement-layer-ghsl
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://human-settlement.emergency.copernicus.eu/documents/GHSL_Data_Package_2023.pdf?t=1727170839
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Product: GHS-BUILT-S, Epoch: 2025, Resolution: 100m, Coordinate system:
    Mollweide, Classification: total - residential (RES) & non residential (NRES)
    classification. (2.0 GB)'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_S_GLOBE_R2023A/GHS_BUILT_S_E2025_GLOBE_R2023A_54009_100/V1-0/GHS_BUILT_S_E2025_GLOBE_R2023A_54009_100_V1_0.zip
  format: null
  id: resource_7e027faf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GHS Built-up Surface
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Product: GHS-POP, Epoch: 2025, Resolution: 100m, Coordinate system:
    Mollweide (4.9 GB)'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/GHS_POP_E2025_GLOBE_R2023A_54009_100/V1-0/GHS_POP_E2025_GLOBE_R2023A_54009_100_V1_0.zip
  format: null
  id: resource_ccceb85f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GHS Population Grid
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-copernicus_globalhumansettlementlaye_2025
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
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: Copernicus Global Human Settlement Layer (GHSL)
version: null
vulnerability: null
---
