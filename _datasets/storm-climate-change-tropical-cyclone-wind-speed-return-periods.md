---
contact_point:
  email: nadia.bloemendaal@vu.nl
  id: attribution_contact
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
creator:
  email: nadia.bloemendaal@vu.nl
  id: attribution_creator
  name: Nadia Bloemendaal
  url: https://vu.nl/en/about-vu/research-institutes/ivm
dataset_id: rdls_hzd-nismod_sdk_stormtcwindspeedcc
description: Gridded tropical-cyclone wind-hazard datasets giving maximum wind speeds
  at fixed return periods (and return periods at fixed wind speeds) at ~10 km resolution
  for each ocean basin, plus companion city/island tables within 100 km; values are
  derived using Weibull plotting formula from STORM climate-change simulations.
details: Datasets were generated with the statistical STORM algorithm using IBTrACS
  as the baseline and adding climate signals from four GCMs (CMCC-CM2-VHR4, CNRM-CM6-1-HR,
  EC-Earth3P-HR, HadGEM3-GC31-HM); outputs are distributed as netCDF (fixed return
  periods or fixed wind speeds, by basin) and Excel workbooks (cities/islands) including
  mean, standard deviation, and 5-95% confidence intervals.
exposure: []
extra_attributions:
- email: info@deltares.nl
  id: attribution_collaborator_1
  name: Deltares,Delft, The Netherlands
  role: collaborator
  url: https://www.deltares.nl/en
- email: pers@knmi.nl
  id: attribution_collaborator_2
  name: Royal Netherlands Meteorological Institute (KNMI), De Bilt, The Netherlands
  role: collaborator
  url: https://www.knmi.nl/over-het-knmi/about
- email: enquiries@bodc.ac.uk
  id: attribution_collaborator_3
  name: University of Southampton, National Oceanography Centre, School of Ocean and
    Earth Science
  role: collaborator
  url: https://noc.ac.uk/
- email: info.ivm@vu.nl
  id: attribution_collaborator_4
  name: Vrije Universiteit Amsterdam, Institute for Environmental Studies (IVM)
  role: collaborator
  url: https://vu.nl/en/about-vu/research-institutes/ivm
- email: angela.wenham@economics.ox.ac.uk
  id: attribution_collaborator_5
  name: Climate Econometrics, Nuffield College, Oxford, UK
  role: collaborator
  url: https://www.nuffield.ox.ac.uk/our-research/research-centres/climate-econometrics/
- email: enquiries@metoffice.gov.uk
  id: attribution_collaborator_6
  name: MetOffice, Exeter, UK
  role: collaborator
  url: https://www.metoffice.gov.uk/
- email: OEP@treasury.gov
  id: attribution_collaborator_7
  name: Office of Macroeconomic Analysis, U.S. Department of the Treasury
  role: collaborator
  url: https://home.treasury.gov/about/offices/economic-policy
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: ''
  intensity: ''
  occurrence_range: 1/10 to 1/10000 years
  processes: ''
  seasonality: ''
license: CC0-1.0
loss: null
project: null
publisher:
  email: researchdata@4tu.nl
  id: attribution_publisher
  name: 4TU.ResearchData
  url: https://data.4tu.nl/
purpose: To provide consistent, high-resolution tropical-cyclone wind hazard metrics
  for present (1979-2014) and near-future (2015-2050) climates that support risk assessment,
  engineering design, and adaptation planning across basins and selected coastal cities
  and islands.
resources:
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c064030c-e60d-4394-9c46-4b1c81c6fe3f
  format: Excel (xlsx)
  id: resource_storm_cities_cmcc
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Cities: TC wind-speed return periods - CMCC-CM2-VHR4'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c97acdc5-ce00-445e-89fb-9eb0854561b7
  format: Excel (xlsx)
  id: resource_storm_cities_cnrm
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Cities: TC wind-speed return periods - CNRM-CM6-1-HR'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4c5743bf-45bb-4930-bd1a-dc1913ba69a9
  format: Excel (xlsx)
  id: resource_storm_cities_ecearth
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Cities: TC wind-speed return periods - EC-Earth3P-HR'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of 18 coastal cities
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/79e8563e-54bf-4d52-a3a0-d5ae04be3a06
  format: Excel (xlsx)
  id: resource_storm_cities_hadgem
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Cities: TC wind-speed return periods - HadGEM3-GC31-HM'
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/2a3759e8-f4ad-4190-abb3-434ad5c4679b
  format: GeoTIFF (tif)
  id: resource_storm_frp_tif_cmcc
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - CMCC-CM2-VHR4
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c460a0c8-f918-4ede-a734-75e77e99b102
  format: GeoTIFF (tif)
  id: resource_storm_frp_tif_cnrm
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - CNRM-CM6-1-HR
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/304d1441-bd71-47c7-8231-b20253c1cc2a
  format: GeoTIFF (tif)
  id: resource_storm_frp_tif_ecearth
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - EC-Earth3P-HR
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/856f9530-56d7-489e-8005-18ae36db4804
  format: GeoTIFF (tif)
  id: resource_storm_frp_tif_hadgem
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - HADGEM3-GC31-HM
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: maximum wind speed (m/s) at fixed return periods on
    ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/9740b235-c2fe-4677-a8b9-f90eb13e4938
  format: GeoTIFF (tif)
  id: resource_storm_frp_tif_median
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (GeoTIFF tiles) - MEDIAN
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/3b7dde9d-bff7-4d96-9024-e8169e8effc0
  format: NetCDF (nc)
  id: resource_storm_frp_grid_cmcc
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (gridded) - CMCC
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/cb4bbaaa-8d70-48f5-865d-d3514ba15503
  format: NetCDF (nc)
  id: resource_storm_frp_grid_cnrm
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (gridded) - CNRM
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/9e5fb7fe-12b9-4197-ad78-e4e0e2b1c754
  format: NetCDF (nc)
  id: resource_storm_frp_grid_ecearth
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (gridded) - EC-Earth
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/5f7fc711-990c-4c95-a071-c17f648d43bb
  format: NetCDF (nc)
  id: resource_storm_frp_grid_hadgem
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (gridded) - HadGEM
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: maximum wind speed (m/s) at fixed return periods
    on ~10 km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/e3b74bbd-04df-4399-ab23-a13af5be4a9b
  format: NetCDF (nc)
  id: resource_storm_frp_grid_median
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Return Periods (gridded) - MEDIAN
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/df247ab2-7565-4888-b5a9-2ccd31d9c90f
  format: GeoTIFF (tif)
  id: resource_storm_fws_tif_cmcc
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - CMCC-CM2-VHR4
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/43ce1a8f-914a-414c-b949-884e06616301
  format: GeoTIFF (tif)
  id: resource_storm_fws_tif_cnrm
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - CNRM-CM6-1-HR
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/ac3fd12d-c21d-406e-8e2e-bd212ee9f817
  format: GeoTIFF (tif)
  id: resource_storm_fws_tif_ecearth
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - EC-Earth3P-HR
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/a7e915a4-ee2a-44d7-8e91-8920bff34f16
  format: GeoTIFF (tif)
  id: resource_storm_fws_tif_hadgem
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - HADGEM3-GC31-HM
- coordinate_system: EPSG:4326
  description: 'GeoTIFF tiles: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/6107d9db-5e6f-4ee7-b113-ce66c1e73aa1
  format: GeoTIFF (tif)
  id: resource_storm_fws_tif_median
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (GeoTIFF tiles) - MEDIAN
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/02773d34-5e47-41be-bf15-5a5c537ae78c
  format: NetCDF (nc)
  id: resource_storm_fws_grid_cmcc
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (gridded) - CMCC
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4b2b73b2-225e-4bcf-af5b-5e048501b354
  format: NetCDF (nc)
  id: resource_storm_fws_grid_cnrm
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (gridded) - CNRM
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/3e489cb4-049c-43d3-ab9e-ab40d9e3f375
  format: NetCDF (nc)
  id: resource_storm_fws_grid_ecearth
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (gridded) - EC-Earth
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/c1da70b1-64d5-4151-aa9c-2ae15bd89de6
  format: NetCDF (nc)
  id: resource_storm_fws_grid_hadgem3
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (gridded) - HadGEM3
- coordinate_system: EPSG:4326
  description: 'Gridded dataset: return period (years) for fixed wind speeds on ~10
    km grids for all ocean basins'
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/6107d9db-5e6f-4ee7-b113-ce66c1e73aa1
  format: NetCDF (nc)
  id: resource_storm_fws_grid_median
  media_type: null
  spatial_resolution: 10000
  temporal: null
  title: STORM Fixed Wind Speeds (gridded) - MEDIAN
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/4a961e63-bb03-4766-ae91-7cf1deb72ff8
  format: Excel (xlsx)
  id: resource_storm_islands_cmcc
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Islands: TC wind-speed return periods - CMCC-CM2-VHR4'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/0632e12d-270e-4496-9bc8-650cb47be71d
  format: Excel (xlsx)
  id: resource_storm_islands_cnrm
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Islands: TC wind-speed return periods - CNRM-CM6-1-HR'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/43396cb0-72bd-46f0-97f2-006a2e31068f
  format: Excel (xlsx)
  id: resource_storm_islands_ecearth
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Islands: TC wind-speed return periods - EC-Earth3P-HR'
- coordinate_system: EPSG:4326
  description: Excel workbook with return periods at fixed wind speeds and wind speeds
    at fixed return periods for events within 100 km of island capitals (SIDS and
    others)
  download_url: https://data.4tu.nl/file/504c838e-2bd8-4d61-85a1-d495bdc560c3/39e5571c-efd1-41ee-a4f2-1d94e792f1ed
  format: Excel (xlsx)
  id: resource_storm_islands_hadgem
  media_type: null
  spatial_resolution: null
  temporal: null
  title: 'STORM Islands: TC wind-speed return periods - HadGEM3-GC31-HM'
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-nismod_sdk_stormtcwindspeedcc
spatial:
  countries:
  - GLO
  scale: global
title: STORM climate change tropical cyclone wind speed return periods
version: '4'
vulnerability: null
---
