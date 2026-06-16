---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth Observation Group
  url: https://eogdata.mines.edu/products/vnl/
creator:
  affiliation: null
  email: null
  name: Earth Observation Group
  url: https://eogdata.mines.edu/products/vnl/
dataset_id: rdls_exp-crstac_viirsnighttimelightsvnl_vnlversion2
description: 'A new consistently processed time series of annual global VIIRS nighttime
  lights has been produced from monthly cloud-free average radiance grids spanning
  2012* to 2020. The new methodology is a modification of the original method based
  on nightly data (Annual VNL V1) [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
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
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: As the pioneer of the nocturnal remote sensing technology, Earth Observation
    Group (EOG) had been collecting nighttime satellite imagery and produce global
    Nighttime Light map with highest quality. The history of Nighttime Light map produced
    by EOG can trace back early as 1994, with the Operational Linescan Sensor (OLS)
    onboard Defense Meteorological Satellite Program (DMSP) satellites. Since the
    launch of the latest generation of earth observation satellite, the Joint Polar-orbiting
    Satellite System (JPSS), the Visible and Infrared Imaging Suite (VIIRS) Day Night
    Band (DNB) on board of JPSS satellites provides astounding improvement on low
    light imaging compared to DMSP-OLS.
  sources: []
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth Observation Group
  url: https://eogdata.mines.edu/products/vnl/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.3390/rs13050922
  id: ref_doi
  name: null
  url: https://doi.org/10.3390/rs13050922
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/viirs-nighttime-lights-vnl/vnl-version-2/vnl-version-2.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: VIIRS Nighttime Lights (VNL) - VNL version 2'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: VIIRS Nighttime Lights (VNL) - VNL version 2 - data file
  download_url: https://eogdata.mines.edu/nighttime_light/annual/v20/
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIIRS Nighttime Lights (VNL) - VNL version 2 - data file
- access_url: https://doi.org/10.3390/rs13050922
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: VIIRS Nighttime Lights (VNL) - VNL version 2 (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_viirsnighttimelightsvnl_vnlversion2
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 463
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '2012'
temporal_resolution: P1Y
title: VIIRS Nighttime Lights (VNL) - VNL version 2
version: null
vulnerability: null
---
