---
contact_point:
  email: mamadio@worldbank.org
  id: '3'
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: '2'
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-GIRI_DR
description: Datasets containing probabilistic analysis of drought using multiple
  indices (SPI, SSI, SMA) covering historical and future climate projections at the
  global scale. Includes return period analysis, event frequency counts, and average
  event duration.
details: 'The drought hazard model uses three complementary indices: Standardized
  Precipitation Index (SPI) for meteorological drought, Standardized Streamflow Index
  (SSI) for hydrological drought, and Soil Moisture Anomaly (SMA) for agricultural
  drought. Each index is analyzed for return periods, number of events, and average
  event duration under historical and projected climate scenarios (SSP1 and SSP5).'
exposure: []
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: drought
  intensity: SMA:-, SPI:-, SSI:-
  occurrence_range: Return period 5 to 25 years
  processes: hydrological_drought, meteorological_drought
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  email: null
  id: '1'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index drought return period analysis for
    historical climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_RP_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SPI Drought (RPs Historical)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index drought return period analysis for
    SSP1 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_RP_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (RPs SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index drought return period analysis for
    SSP5 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_RP_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (RPs SSP5)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index drought return period analysis for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_RP_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SSI Drought (RPs Historical)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index drought return period analysis for SSP1
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_RP_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (RPs SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index drought return period analysis for SSP5
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_RP_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (RPs SSP5)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly drought return period analysis for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_RP_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SMA Drought (RPs Historical)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly drought return period analysis for SSP1 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_RP_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (RPs SSP1)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly drought return period analysis for SSP5 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_RP_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (RPs SSP5)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index number of drought events for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_NEV_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SPI Drought (# events Historical)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index number of drought events for SSP1
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_NEV_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (# events SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index number of drought events for SSP5
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_NEV_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (# events SSP5)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index number of drought events for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_NEV_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SSI Drought (# events Historical)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index number of drought events for SSP1 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_NEV_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (# events SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index number of drought events for SSP5 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_NEV_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (# events SSP5)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly number of drought events for historical climate
    (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_NEV_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SMA Drought (# events Historical)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly number of drought events for SSP1 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_NEV_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (# events SSP1)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly number of drought events for SSP5 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_NEV_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (Number of Events - SSP5)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index average drought duration for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_DUR_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SPI Drought (Average Duration - Historical)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index average drought duration for SSP1
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_DUR_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (Average Duration - SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Precipitation Index average drought duration for SSP5
    climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SPI_DUR_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SPI Drought (Average Duration - SSP5)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index average drought duration for historical
    climate (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_DUR_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SSI Drought (Average Duration - Historical)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index average drought duration for SSP1 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_DUR_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (Average Duration - SSP1)
- coordinate_system: EPSG:4326
  description: Standardized Streamflow Index average drought duration for SSP5 climate
    projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SSI_DUR_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SSI Drought (Average Duration - SSP5)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly average drought duration for historical climate
    (1979-2016)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_DUR_HST
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2016'
    start: '1979'
    temporal_resolution: null
  title: SMA Drought (Average Duration - Historical)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly average drought duration for SSP1 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_DUR_SSP1
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (Average Duration - SSP1)
- coordinate_system: EPSG:4326
  description: Soil Moisture Anomaly average drought duration for SSP5 climate projection
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: SMA_DUR_SSP5
  media_type: null
  spatial_resolution: 5000
  temporal:
    duration: null
    end: '2100'
    start: '2017'
    temporal_resolution: null
  title: SMA Drought (Average Duration - SSP5)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-GIRI_DR
spatial:
  countries:
  - GLO
  scale: global
title: Global drought hazard
version: '1'
vulnerability: null
---
